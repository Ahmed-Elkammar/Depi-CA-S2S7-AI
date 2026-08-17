class Task1:
    def __init__(self, number: int):
        self.number = number

    def multiplication_table(self) -> None:
        for i in range(1, 11):
            print(f"{self.number} x {i} = {self.number * i}")


task1 = Task1(5)
task1.multiplication_table()