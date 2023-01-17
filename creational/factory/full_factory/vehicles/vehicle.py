from abc import ABC, abstractmethod


class Vehicle(ABC):
    _name: str

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @abstractmethod
    def start(self):
        return NotImplementedError

    @abstractmethod
    def stop(self):
        return NotImplementedError
