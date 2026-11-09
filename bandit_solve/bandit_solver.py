
from pathlib import Path

from bandit_solve.authentication_method import AuthenticationMethod

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
    # - Formally define class
    # - Make base authentication method class which password, kepair, and other stuff will inherit from
    # - Expand the thing as needed
    # - Make a better design

    def _construct_file_path(self):
        print()
        next_level = self.current_level + 1
        script_filename = f'solver_{self.current_level}_{next_level}.sh'
        path =  Path(f'./{SOLVER_SCRIPT_DIR}') / script_filename
        return str(path.resolve())
    
        pass

    @property
    def current_level(self) -> int:
        return self._current_level

    def __init__(self, auth_method: AuthenticationMethod, current_level: int = 0, hostname=HOSTNAME, port = PORT):
        """
        ## TODO:
         - Write me
        """
        self._current_level = current_level
        self._auth_method = auth_method
        self._hostname = hostname
        self._port = port