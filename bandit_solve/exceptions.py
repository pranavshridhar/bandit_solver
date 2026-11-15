
class SolverNotFound(Exception):

    def __init__(self, filepath: str, level: int, message="Solver for this level not found."):
        self.message = message
        self.filepath = filepath
        self.level = level
        super().__init__(self.message)

    def __str__(self):
        return f"Level {self.level}->{self.level+1}: {self.message} Create a solver script for this level with path: {self.filepath}"

