;buildInfoPackage: chisel3, version: 3.2.0, scalaVersion: 2.12.10, sbtVersion: 1.3.2
circuit ComposedModule : 
  module Add : 
    input clock : Clock
    input reset : Reset
    output io : {flip a : UInt<4>, flip b : UInt<4>, out : UInt<4>}
    
    node _T = add(io.a, io.b) @[ModA.sc 20:18]
    node _T_1 = tail(_T, 1) @[ModA.sc 20:18]
    io.out <= _T_1 @[ModA.sc 20:10]
    
  module ComposedModule : 
    input clock : Clock
    input reset : UInt<1>
    output io : {flip a : UInt<4>, flip b : UInt<4>, flip c : UInt<4>, out : UInt<4>}
    
    inst addr of Add @[cmd4.sc 8:22]
    addr.clock <= clock
    addr.reset <= reset
    addr.io.a <= io.a @[cmd4.sc 9:15]
    addr.io.b <= io.b @[cmd4.sc 10:15]
    node _T = add(addr.io.out, io.c) @[cmd4.sc 11:27]
    node _T_1 = tail(_T, 1) @[cmd4.sc 11:27]
    io.out <= _T_1 @[cmd4.sc 11:12]
    
