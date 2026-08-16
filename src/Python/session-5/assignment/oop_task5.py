class Task5:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def is_perfect(self, number: int) -> bool:
        total = 0

        for i in range(1, number):
            if number % i == 0:
                total += i

        return total == number

    def find_perfect_numbers(self) -> list:
        perfect_numbers = []

        for number in range(self.start, self.end + 1):
            if self.is_perfect(number):
                perfect_numbers.append(number)

        return perfect_numbers


task5 = Task5(1, 10000)
print(task5.find_perfect_numbers())