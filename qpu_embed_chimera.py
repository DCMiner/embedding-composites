from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import sys

# Set up the QUBO. Start with the equations for the three qubits:
# x + y - 2xy -1
# 2yz - y - z
# -2zx + z + x - 1
# QUBO: 2x - 2xy + 2yz - 2zx - 2

chainstrength = float(sys.argv[1])
numruns = 1000
Q = {(0, 0): 2, (0, 1): -2, (0, 2): -2, (1, 2): 2}

sampler = EmbeddingComposite(DWaveSampler(solver={'topology__type__eq': 'chimera'}))
response = sampler.sample_qubo(Q, chain_strength=chainstrength, num_reads=numruns)

for smpl, energy in response.data(['sample', 'energy']):
    print(smpl, energy)
