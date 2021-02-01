;buildInfoPackage: chisel3, version: 3.2.0, scalaVersion: 2.12.10, sbtVersion: 1.3.2
circuit Add : 
  module Add : 
    input clock : Clock
    input reset : UInt<1>
    output io : {flip a : UInt<4>, flip b : UInt<4>, out : UInt<4>}
    
    node _T = add(io.a, io.b) @[ModA.sc 20:18]
    node _T_1 = tail(_T, 1) @[ModA.sc 20:18]
    io.out <= _T_1 @[ModA.sc 20:10]
    
