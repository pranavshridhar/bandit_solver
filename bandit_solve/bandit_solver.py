
from pathlib import Path
import sys
from typing import Optional
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import AuthenticationException

from bandit_solve.authentication_method import AuthenticationMethod, Password
from bandit_solve.file_utils import read_file

# default vars
SOLVER_SCRIPT_DIR = "solver_scripts"
HOSTNAME = "bandit.labs.overthewire.org"
PORT = 2220

class Solver:
    """
    A SolverSession is the object responsible for solving a level.
    Given the authentication method into a level, its `solve()` function
    executes the related solver script to obtain the authentication method
    to the next level.
    """
    # TODO: Lots of shit
    # - Expand the thing as needed
    # - Make a better design

    @property
    def solver_path(self):
        next_level = self.current_level + 1
        script_filename = f'solve_{self.current_level}_{next_level}.sh'
        path =  Path(f'./{SOLVER_SCRIPT_DIR}') / script_filename
        return str(path.resolve())

    @property
    def current_level(self) -> int:
        return self._current_level

    def __init__(
            self, 
            auth_method: AuthenticationMethod, 
            current_level: int = 0, 
            hostname=HOSTNAME, 
            port = PORT,
            ssh_client: Optional[SSHClient] = None
        ):
        """
        ## TODO:
         - Write me
        """
        self._current_level = current_level
        self._auth_method = auth_method
        self._hostname = hostname
        self._port = port
        self._ssh_client = ssh_client if ssh_client is not None else SSHClient()
        self._ssh_client.set_missing_host_key_policy(AutoAddPolicy())

    @property
    def _level_user(self):
        return f'bandit{self._current_level}'

    def solve(self) -> AuthenticationMethod:

        ssh = self._ssh_client
        auth = self._auth_method
        script_contents = read_file(self.solver_path)

        try:

            ssh.connect(
                hostname=self._hostname,
                port=self._port,
                username=self._level_user,
                look_for_keys=False,
                allow_agent=False,
                **auth.paramiko_kwargs
            )
        except AuthenticationException:
            print(f"ERROR: Authentication into level {self.current_level} (bandit{self.current_level}) failed. Please check authentication method or solution to previous problem.")
            raise
            

        stdin, stdout, stderr = ssh.exec_command('/bin/bash')
        stdin.write(script_contents)
        raw_auth = stdout.read().decode()
        return Password(self.current_level+1, raw_auth) # TODO: Account for private key possibility
