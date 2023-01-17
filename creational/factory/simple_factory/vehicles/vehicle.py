from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        return NotImplementedError

    @abstractmethod
    def stop(self):
        return NotImplementedError
