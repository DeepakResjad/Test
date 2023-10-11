'''7. Write a program that generates the Collatz sequence for a given number n. The Collatz
sequence starts with a positive integer n and generates the next term in the sequence as
follows: If n is even, the next term is n/2; if n is odd, the next term is 3n + 1. Series ends
with a number 1. '''

def collatz(n): 
    if n <= 0:
        print("Please enter a positive number.") 
    col_series = []
    while n>1:
        if n%2==0:
            n = n//2
        else:
            n = 3*n+1
        col_series.append(n)
    return col_series

n = int(input("Enter a positive number: "))
print("Collatz Series: ", collatz(n))
            

