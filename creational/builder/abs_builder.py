from abc import ABC, abstractmethod

from creational.builder.computer import Computer


class AbsBuilder(ABC):
    _computer: Computer

    def get_computer(self):
        return self._computer

    def new_computer(self):
        self._computer = Computer()

    @abstractmethod
    def build_mainboard(self):
        raise NotImplementedError

    @abstractmethod
    def get_case(self):
        raise NotImplementedError

    @abstractmethod
    def install_mainboard(self):
        raise NotImplementedError

    @abstractmethod
    def install_hard_drive(self):
        raise NotImplementedError

    @abstractmethod
    def install_video_card(self):
        raise NotImplementedError
