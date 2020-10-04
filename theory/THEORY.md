## Theory

The current library uses the Miller primality test<sup>(1)</sup> with known strong pseudoprime bases<sup>(2)</sup> to provide deterministic testing for integers between 2 and 2^64 - 1<sup>(3)</sup>.

1. Miller, G. (1976), ["Riemann's Hypothesis and Tests for Primality"](https://core.ac.uk/download/pdf/82649441.pdf), Journal of Computer and System Sciences.

1. Zhang, Z and Tang, M. (2003), ["Finding strong pseudoprimes to several bases. II"](http://www.jointmathematicsmeetings.org/mcom/2003-72-244/S0025-5718-03-01545-X/S0025-5718-03-01545-X.pdf), Mathematics of Computation. 

1. McCraine, J. (1997), ["Sequence A014233 (Smallest odd number for which Miller-Rabin primality test on bases <= n-th prime does not reveal compositeness)"](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test), The On-Line Encyclopedia of Integer Sequences, OEIS Foundation. 
