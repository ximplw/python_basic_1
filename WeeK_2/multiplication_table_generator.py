#Multiplication Taable Generator
class Multiplication_Table:
    def __init__(self, number, limit):
        self.number = number
        self.limit = limit
        
    def generate_table(self):
        table = []
        for i in range(1, self.limit + 1):
            table.append(f"{self.number} x {i} = {self.number * i}")
        return table
    
if __name__ == "__main__":
    num = int(input("Enter the number to generate multiplication table: "))
    lim = int(input("Enter the limit up to which multiplication table is to be generated: "))
    
    multiplication_table = Multiplication_Table(num, lim)
    generated_table = multiplication_table.generate_table()

    print(f"Multiplication table of {num} up to {lim} is:  ")

    for row in generated_table:
        print(row)
