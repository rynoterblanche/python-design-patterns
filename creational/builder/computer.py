class Computer:
    case: str
    mainboard: str
    cpu: str
    memory: str
    hard_drive: str
    video_card: str

    def display(self):
        print(self)

    def __str__(self):
        return f"Custom Computer:" \
               f"\n\t{'Case':>11}: {self.case}" \
               f"\n\t{'Mainboard':>11}: {self.mainboard}" \
               f"\n\t{'CPU':>11}: {self.cpu}" \
               f"\n\t{'Memory':>11}: {self.memory}" \
               f"\n\t{'Hard Drive':>11}: {self.hard_drive}" \
               f"\n\t{'Video Card':>11}: {self.video_card}"
