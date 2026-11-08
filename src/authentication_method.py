from abc import ABC, abstractmethod


class AuthenticationMethod(ABC):

    @abstractmethod
    def paramiko_kwargs(self) -> dict:
        pass

    @abstractmethod
    def suggested_filename(self) -> str:
        pass



