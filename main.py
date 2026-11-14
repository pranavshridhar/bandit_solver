import copy
from typing import List

import paramiko
from paramiko.client import SSHClient

from bandit_solve.authentication_method import AuthenticationMethod, Password
from bandit_solve.bandit_solver import Solver
from bandit_solve.file_utils import read_file, write_file

# ssh = SSHClient()

# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# with open("solver_scripts/solve_0_1.sh") as f:
#     script = f.read()


# ssh.connect(
#     hostname='bandit.labs.overthewire.org',
#     port=2220,
#     username='bandit0',
#     password='bandit0',
#     allow_agent=False,
#     look_for_keys=False
# )

# stdin, stdout, stderr = ssh.exec_command('/bin/bash')
# stdin.write(script)
# stdin.close()

# stdout.read().decode()

LEVELS = 2


ssh = SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

auth: AuthenticationMethod = Password(0, "bandit0")
auth_data: List[AuthenticationMethod] = []

try:
    for i in range(LEVELS):
        solver = Solver(auth, current_level=i)
        auth = solver.solve()
        auth_data.append(copy.deepcopy(auth))
        print(f"cracked level: {i}")

    print(f"reached the end of {LEVELS} levels")
except Exception as e:
    print(e)
finally:
    print("saving obtained auth data to disk...")
    for auth in auth_data:
        filename = auth.suggested_filename
        write_file(filename, auth.raw)
    print("data saved.")








