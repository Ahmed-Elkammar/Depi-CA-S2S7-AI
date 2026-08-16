class Task4:
    def __init__(self, number: int):
        self.number = number

    def decimal_to_binary(self) -> str:
        if self.number == 0:
            return "0"

        number = self.number
        binary = []

        while number > 0:
            remainder = number % 2
            binary.append(str(remainder))
            number //= 2

        binary.reverse()

        return "".join(binary)


task4 = Task4(10)
print(task4.decimal_to_binary())