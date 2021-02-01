// AUTOGENERATED! DO NOT EDIT! File to edit: nbs/test.ipynb (unless otherwise specified).

// Cell
//default_exp test
import $file.^.source.load_ivy

// Cell
import chisel3.{Input => Input}
import chisel3._
import chisel3.util._
import chisel3.tester._
import chisel3.iotesters.{ChiselFlatSpec, Driver, PeekPokeTester}
import chisel3.tester.RawTester.test

// Cell
class ALUIO extends Bundle {
    val a = Input(UInt(4.W))
    val b = Input(UInt(4.W))
    val out = Output(UInt(4.W))
}

// Cell
class ALUSkeleton extends Module {
    val io = IO(new ALUIO)
}

// Cell
class Add(m: ALUSkeleton) {
    def add(a: UInt, b: UInt): UInt = a + b
}

// Cell
class Sub(m: ALUSkeleton) {
    def sub(a: UInt, b: UInt): UInt = a - b
}

// Cell
class MulDiv(m: ALUSkeleton) {
    def mul(a: UInt, b: UInt): UInt = a * b
    def div(a: UInt, b: UInt): UInt = a / b
}

// Cell
implicit def includeAdd(m: ALUSkeleton) = new Add(m)
implicit def includeSub(m: ALUSkeleton) = new Sub(m)
implicit def includeMulDiv(m: ALUSkeleton) = new MulDiv(m)

// Cell
// This Operator module perform 1 type of operation depending on 'op' parameter
class Operator(op: String) extends ALUSkeleton {
    op match {
        // Call on the implicit function
        case "+" => io.out := this.add(io.a, io.b)
        case "-" => io.out := this.sub(io.a, io.b)
        case "*" => io.out := this.mul(io.a, io.b)
        case "/" => io.out := this.div(io.a, io.b)
        case _ => io.out := 0.U
    }
}