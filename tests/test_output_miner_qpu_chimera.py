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
import os
import subprocess
import unittest

example_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestSmoke(unittest.TestCase):
    # test that the example runs without failing
    def test_smoke(self):
        file_path = os.path.join(example_dir, 'miner_qpu_chimera.py')

        value = subprocess.check_output(["python", file_path, "4"])

        # Check the expected energy
        str1 = '{0: 0, 1: 0, 2: 1} -2.0'
        str2 = '{0: 1, 1: 1, 2: 1} -2.0'
        str3 = '{0: 0, 1: 0, 2: 0} -2.0'
        str4 = '{0: 1, 1: 1, 2: 0} -2.0'
        str5 = '{0: 0, 1: 1, 2: 0} -2.0'
        str6 = '{0: 1, 1: 0, 2: 1} -2.0'
        self.assertTrue(str1 in str(value))
        self.assertTrue(str2 in str(value))
        self.assertTrue(str3 in str(value))
        self.assertTrue(str4 in str(value))
        self.assertTrue(str5 in str(value))
        self.assertTrue(str6 in str(value))

if __name__ == '__main__':
    unittest.main()
