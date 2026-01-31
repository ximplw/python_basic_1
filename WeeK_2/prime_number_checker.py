#Prime number checker 
class PrimeNumberChecker:
    
    def __init__(self, number):
        self.number = number

    def is_Prime(self):
        count= 0
        for i in range(1, self.number+1):
            if self.number % i == 0:
                count += 1
        if count == 2:
            print(f"{self.number} is a prime number.")

        else:
            print(f"{self.number} is not a prime number.") 

if __name__== "__main__":

    num = int(input("Enter a number to check if it is prime: "))

    prime_checker = PrimeNumberChecker(num)
    prime_checker.is_Prime()