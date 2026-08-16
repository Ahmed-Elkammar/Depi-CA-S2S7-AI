class Task3:
    def __init__(self, number: int):
        self.number = number

    def prime_factors(self) -> list:
        factors = []
        number = self.number
        divisor = 2

        while number > 1:
            while number % divisor == 0:
                factors.append(divisor)
                number //= divisor

            divisor += 1

        return factors


task3 = Task3(56)
print(task3.prime_factors())