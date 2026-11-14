import copy
from typing import List

import paramiko
from paramiko.client import SSHClient

from bandit_solve.authentication_method import AuthenticationMethod, Password
from bandit_solve.bandit_solver import Solver
from bandit_solve.file_utils import read_file, write_file

LEVELS = 20


ssh = SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

auth: AuthenticationMethod = Password(0, "bandit0")
auth_data: List[AuthenticationMethod] = []

try:
    for i in range(LEVELS):
        solver = Solver(auth, current_level=i)
        auth = solver.solve()
        auth_data.append(copy.deepcopy(auth))

        # CONSIDER: maybe don't use the word 'cracked' here?
        print(f"cracked level: {i+1}")

    print(f"reached the end of {LEVELS} levels")
except Exception as e:
    print(e)
finally:
    print("saving obtained auth data to disk...")
    for auth in auth_data:
        filename = auth.suggested_filename
        write_file(filename, auth.raw)
    print("data saved.")








