from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError
