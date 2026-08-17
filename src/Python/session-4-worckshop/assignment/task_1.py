#Write a function that inputs a number and prints the multiplication table of that number 

def multiplication_table(number : int) -> None:
    i = 0
    while i <10:
        print(f"{number}*{i}={number * i}")
        i += 1



def main ():
    num = int(input("enter your number :"))
    multiplication_table(num)


main()