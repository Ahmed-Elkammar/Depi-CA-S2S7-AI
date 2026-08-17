#Write a program to print twin primes less than 1000.
# If two consecutive odd numbers are both prime then they are known as twin primes 
def Twin_prime():
    for i in range(3,1000,2):
        prime1 = True
        prime2 =True
        for j in range(2,i):
            if i % j == 0 :
                prime1 = False
            if (i+2) % j ==0:
                prime2 = False

        if prime1 and prime2 :
                print(i,"and",i+2,"are twin prime")

def main():
    Twin_prime()
main()
