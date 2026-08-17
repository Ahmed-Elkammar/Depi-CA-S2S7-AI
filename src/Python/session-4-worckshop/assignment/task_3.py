# Write a program to find out the prime factors of a number.
def prime_factor(num :int)->list:
    list = []
    for i in range (2 , num + 1 ):
        while num % i ==0:
            list.append(i)
            num = num // i
            

    return list

def main():

    number = int(input("enter your number : "))
    print (prime_factor(number))


main()