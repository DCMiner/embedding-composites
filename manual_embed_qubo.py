# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import dimod
import sys
from dwave.system.samplers import DWaveSampler

# Friends and enemies problem on a triangle, in QUBO
# Do the embedding manually

# Use qubits 0, 1, 4, 5
#
# Constrain qubits 0 and 4 to have the same value
# q_0 + q_4 - 2 q_0 q_4
#
# Constrain qubits 1 and 4 to have opposite values - but notice that we're
# going to embed qubits 1 and 5 to have the same value
# 2 q_1 q_4 - q_4 - 0.5 (q_1 + q_5) + 1
#
# Constrain qubits 0 and 5 to have the same value - and yes, we will embed
# 1 and 5 to have the same value
# q_0 + 0.5 (q_1 + q_5) - 2 q_0 q_5
#
# Constrain qubits 1 and 5 to have the same value, explicitly
# chainstrength (q_1 + q_5 - 2q_1 q_5)

numruns = 1000
chainstrength = float(sys.argv[1])
sampler = DWaveSampler(solver={'qpu': True})

# Add all the equations together
Q = {(0, 0): 2, 
     (1, 1): chainstrength,
     (5, 5): chainstrength,
     (0, 4): -2,
     (1, 4): 2,
     (0, 5): -2,
     (1, 5): -2 * chainstrength}

bqm = dimod.BinaryQuadraticModel.from_qubo(Q, offset=1)

results = sampler.sample(bqm, num_reads=numruns)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
