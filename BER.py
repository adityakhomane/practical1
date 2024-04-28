import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt
np.random.seed(100)
np.random.randn(200)
N = 10**6
ip = np.random.randint(2, size=N)
s = 2*ip - 1
n = 1/np.sqrt(2)*(np.random.randn(N) + 1j*np.random.randn(N))
Eb_N0_dB = np.arange(-3, 11, 1)
nErr = np.zeros(len(Eb_N0_dB))
for ii in range(len(Eb_N0_dB)):
 y = s + 10**(-Eb_N0_dB[ii]/20)*n
 ipHat = np.real(y) > 0
nErr[ii] = np.sum(ip != ipHat)
simBer = nErr/N
theoryBer = 0.5*erfc(np.sqrt(10**(Eb_N0_dB/10)/2))
plt.figure()
plt.semilogy(Eb_N0_dB, theoryBer, 'b.-', label='theory')
plt.semilogy(Eb_N0_dB, simBer, 'mx-', label='simulation')
plt.axis([-3, 10, 10**-5, 0.5])
plt.grid(True)
plt.legend(loc='upper right')
plt.xlabel('Eb/No, dB')
plt.ylabel('Bit Error Rate')
plt.title('Bit error probability curve for BPSK modulation')
plt.show()
