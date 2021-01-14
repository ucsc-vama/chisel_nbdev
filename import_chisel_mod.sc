import $file.source.load_ivy

import chisel3.{Input => Input}
import chisel3._
import chisel3.util._
import chisel3.tester._
import chisel3.iotesters.{ChiselFlatSpec, Driver, PeekPokeTester}
import chisel3.tester.RawTester.test

import $file.ToImport, ToImport._

test(new Add) { c =>
    c.io.a.poke(1.U)    
    c.io.b.poke(2.U)    
    c.clock.step(1)    
    c.io.out.expect(3.U)
    
    c.io.a.poke(5.U)    
    c.io.b.poke(2.U)    
    c.clock.step(1)    
    c.io.out.expect(7.U)
}

class ComposedModule extends Module {
    val io = IO(new Bundle {
        val a = Input(UInt(4.W))
        val b = Input(UInt(4.W))
        val c = Input(UInt(4.W))
        val out = Output(UInt(4.W))
    })
    val addr = Module(new Add)    
    addr.io.a := io.a
    addr.io.b := io.b
    io.out := addr.io.out + io.c
}

test(new ComposedModule) { c =>
    c.io.a.poke(1.U)    
    c.io.b.poke(2.U)    
    c.io.c.poke(3.U)    
    c.clock.step(1)    
    c.io.out.expect(6.U)
    
    c.io.a.poke(5.U)    
    c.io.b.poke(2.U)    
    c.io.c.poke(7.U)    
    c.clock.step(1)    
    c.io.out.expect(14.U)
}


