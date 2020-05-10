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

## ------- import packages -------
from dwave.system import DWaveSampler, EmbeddingComposite

def get_token():
    '''Return your personal access token'''
    
    # TODO: Enter your token here
    return 'YOUR-TOKEN-HERE'

# TODO:  Add code here to define your QUBO dictionary
def get_qubo():
    """Returns a dictionary representing a QUBO"""

    Q = {}

    # Add QUBO construction here
    
    return Q

# TODO:  Choose QPU parameters in the following function
def run_on_qpu(Q, sampler):
    """Runs the QUBO problem Q on the sampler provided.

    Args:
        Q(dict): a representation of a QUBO
        sampler(dimod.Sampler): a sampler that uses the QPU
    """

    chainstrength = 1 # update
    numruns = 1 # update

    sample_set = sampler.sample_qubo(Q, 
                                     chain_strength=chainstrength, 
                                     num_reads=numruns)

    return sample_set


## ------- Main program -------
if __name__ == "__main__":

    token = get_token()

    ## ------- Set up our QUBO dictionary -------

    Q = get_qubo()

    ## ------- Run our QUBO on the QPU -------

    sampler = EmbeddingComposite(DWaveSampler(
                                 endpoint='https://cloud.dwavesys.com/sapi/', 
                                 token=token, 
                                 solver={'qpu': True}))

    sample_set = run_on_qpu(Q, sampler)

    ## ------- Return results to user -------
    for sample, energy in sample_set.data(['sample', 'energy']):
        print(sample, energy)
