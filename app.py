n = int(input("Enter a number n to generate the Fibonacci sequence: "))

# Error handling
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    print("The first", n, "Fibonacci numbers are:")
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b