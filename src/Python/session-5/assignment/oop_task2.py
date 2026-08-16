class Task2:
    def __init__(self, limit: int):
        self.limit = limit

    def is_prime(self, number: int) -> bool:
        if number < 2:
            return False

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False

        return True

    def find_twin_primes(self) -> None:
        for number in range(3, self.limit, 2):
            if self.is_prime(number) and self.is_prime(number + 2):
                print(number, number + 2)


task2 = Task2(1000)
task2.find_twin_primes()