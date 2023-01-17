from creational.builder.budget_box_builder import BudgetBoxBuilder
from creational.builder.director import Director
from creational.builder.highend_box_builder import HighEndBoxBuilder

print("\nBuild a budget box:")
computer_builder = Director(BudgetBoxBuilder())
computer_builder.build_computer()
budget_box = computer_builder.get_computer()
budget_box.display()

print("\nBuild a high end box:")
computer_builder = Director(HighEndBoxBuilder())
computer_builder.build_computer()
box = computer_builder.get_computer()
box.display()
