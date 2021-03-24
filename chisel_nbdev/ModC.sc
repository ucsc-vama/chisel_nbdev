// AUTOGENERATED! DO NOT EDIT! File to edit: nbs/import_composed_mod.ipynb (unless otherwise specified).

// Cell
//default_exp ModC
//package ComposedExample

// Cell
import $file.^.nbdev.ModB, ModB._

// Cell
import $file.^.source.load_ivy

// Cell
import chisel3.{Input => Input}
import chisel3._
import chisel3.util._
import chisel3.tester._
import chisel3.iotesters.{ChiselFlatSpec, Driver, PeekPokeTester}
import chisel3.tester.RawTester.test

// Cell
class DoubleComposedMod extends Module {
    val io = IO(new Bundle {
        val in = Input(UInt(4.W))
        val out = Output(UInt(4.W))
    })

    val composed = Module(new ComposedModule)
    composed.io.a := 1.U
    composed.io.b := 2.U
    composed.io.c := 3.U

    io.out := composed.io.out + io.in
}