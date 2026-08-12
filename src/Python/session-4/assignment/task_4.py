# Write a function that converts a decimal number to binary number 
def decToBin(num: int)->list:
    binary = []
    while num > 0:
        reminder = num % 2
        num //=2 
        binary.append(reminder)
    binary.reverse()
    return binary

def main():
    num = int(input("enter the number : "))
    print(decToBin(num))

main()