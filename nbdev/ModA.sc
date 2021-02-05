// AUTOGENERATED! DO NOT EDIT! File to edit: nbs/test.ipynb (unless otherwise specified).

// Cell
//default_exp ModA

// Cell
import $file.^.source.load_ivy

// Cell
import chisel3.{Input => Input}
import chisel3._
import chisel3.util._
import chisel3.iotesters.{ChiselFlatSpec, Driver, PeekPokeTester}

// Cell
// Chisel Code: Declare a new module definition
class Add extends Module {
  val io = IO(new Bundle {
    val a = Input(UInt(4.W))
    val b = Input(UInt(4.W))
    val out = Output(UInt(4.W))
  })
  io.out := io.a + io.b
}

// Comes from test.ipynb, cell
def FuncFromTest(): Unit = {}