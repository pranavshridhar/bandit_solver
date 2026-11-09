from abc import ABC, abstractmethod
from pathlib import Path


# TODO:
# - Always a cleaner way to implement this.
# - Writing docstring is a good habit
# - Fun problem: try to NOT write to disk.

class AuthenticationMethod(ABC):
    # TODO: Add docstring to explain this
    
    def __init__(self, level: int):
        self._level = level

    @property
    @abstractmethod
    def paramiko_kwargs(self) -> dict:
        pass

    @property
    @abstractmethod
    def suggested_filename(self) -> str:
        pass


class Password(AuthenticationMethod):
    # TODO: Give a better docstring
    """
    Password is an authentication method that will hold a literal string.
    This needs to be passed as a string, so this is easy.
    """

    def __init__(self, level: int, password_text):
        super().__init__(level)
        self._password_text = password_text

    @property
    def paramiko_kwargs(self) -> dict:
        return {"password": self._password_text}

    @property
    def suggested_filename(self) -> str:
        fpath = Path(f'./auths') / 'passwords' / f'bandit{self._level}.txt'
        return str(fpath.resolve())


class PrivateKey(AuthenticationMethod):
    """
    PrivateKey is an authentication method that will hold more information about the private key
    than Password does about a password.
    Paramiko really prefers that we source the private key as an actual file, so that's exactly why we abstract kwargs method.
    """
    # TODO: Add docstring to explain this
    # TODO: Account for possibility of not storing private key as file for the purpose of blazing through all levels

    def __init__(self, level, raw_key: str):
        super().__init__(level)
        self._raw_key = raw_key

    @property
    def suggested_filename(self) -> str:
        fpath = Path(f'./auths') / 'private_keys' / f'bandit{self._level}_key.private'
        return str(fpath.resolve())

    @property
    def paramiko_kwargs(self) -> dict:
        # TODO: assumes we will always store as file. what if we won't?
        return {"key_filename": self.suggested_filename}

