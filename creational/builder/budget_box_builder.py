from creational.builder.abs_builder import AbsBuilder


class BudgetBoxBuilder(AbsBuilder):

    def build_mainboard(self):
        self._computer.mainboard = "MSI"
        self._computer.cpu = "Intel Core i5"
        self._computer.memory = "2 x 8 GB"

    def get_case(self):
        self._computer.case = "Coolermaster"

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = "SSD 1TB"

    def install_video_card(self):
        self._computer.video_card = "RTX 2070"
