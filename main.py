import paramiko
from paramiko.client import SSHClient

from bandit_solver import Solver

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

solver = Solver(current_level=0)
print(solver._construct_file_path())
