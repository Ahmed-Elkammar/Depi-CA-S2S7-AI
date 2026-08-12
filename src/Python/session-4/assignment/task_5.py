#  Write a program to print all the perfect numbers in a given range 

def perfectNums(first : int,second : int) -> None:
    for num in range(first, second + 1):
        total = 0

        for i in range(1, num):
            if num % i == 0:
                total += i

        if total == num:
            print(num)
def main():
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))
    perfectNums(start,end)

main()