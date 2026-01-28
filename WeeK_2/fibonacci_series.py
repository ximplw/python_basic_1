#Program to print Fibonacci series up to n terms

class Fibonacci_Series:
    def __init__(self, n):
        self.n = n

    def generate_seies(self):
        a, b = 0, 1
        roll = []
        for _ in range(self.n):
            roll.append(a)
            a, b = b, a + b
        return roll

if __name__ == "__main__":
    n_terms = int(input("Enter the number of terms in Fibonacci series: "))
    fibonacci_series = Fibonacci_Series(n_terms)
    generated_series = fibonacci_series.generate_seies()
    print(f"Fibonacci series up to {n_terms} terms are: {generated_series}")       
        