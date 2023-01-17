from creational.builder.abs_builder import AbsBuilder


class HighEndBoxBuilder(AbsBuilder):

    def build_mainboard(self):
        self._computer.mainboard = "Gigabyte B@d@ss"
        self._computer.cpu = "Intel Core i9"
        self._computer.memory = "2 x 32 GB"

    def get_case(self):
        self._computer.case = "Coolermaster Supreme Airflow"

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = "SSD 2TB"

    def install_video_card(self):
        self._computer.video_card = "RTX 4090"
