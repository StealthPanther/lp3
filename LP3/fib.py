# Non-recursive Fibonacci
def fibonacciIterative(n):
    first = 0
    second = 1

    print("Fibonacci using non-recursive approach:")
    for i in range(n):
        print(first, end=" ")
        next = first + second
        first = second
        second = next

    print()


# Recursive Fibonacci
def fibonacciRecursive(n):
    if n <= 1:
        return n

    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)


# Main program
n = int(input("Enter the value of n: "))

if n < 0 or n > 45:
    print("Please enter n between 0 and 45")
else:
    fibonacciIterative(n)

    print("Fibonacci using recursive approach:")
    for i in range(n):
        print(fibonacciRecursive(i), end=" ")