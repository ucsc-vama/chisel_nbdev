import $file.source.load_ivy

import chisel3.{Input => Input}
import chisel3._
import chisel3.util._
import chisel3.iotesters.{ChiselFlatSpec, Driver, PeekPokeTester}

// Chisel Code: Declare a new module definition
class Add extends Module {
  val io = IO(new Bundle {
    val a = Input(UInt(4.W))
    val b = Input(UInt(4.W))
    val out = Output(UInt(4.W))
  })
  io.out := io.a + io.b
}




