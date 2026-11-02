# Recursive Fibonacci using Memoization
def recursive_fib_memo(n, memo):
    if n <= 1:
        return n  # Base case: return 0 or 1

    if n in memo:
        return memo[n]  # Return previously calculated value

    # Store the Fibonacci result to avoid recalculation
    memo[n] = recursive_fib_memo(n-1, memo) + recursive_fib_memo(n-2, memo)

    return memo[n]

# Simple Recursive Fibonacci
def recursive_fib(n):
    if n <= 1:
        return n  # Base case
    # Calculate Fibonacci using two previous terms
    return recursive_fib(n-1) + recursive_fib(n-2)

# Non-Recursive (Iterative) Fibonacci
def non_recursive_fib(n):
    a, b = 0, 1  # Initialize first two Fibonacci numbers
    print("Non-Recursive Method: ")
    # Generate Fibonacci series using a loop
    for _ in range(n):
        print(a, end="  ")
        a, b = b, a+b  # Update the two numbers

# Accept the number of terms
n = int(input())

# Display menu options
memo = {}
print("1:- Non Recursive Method\n2:- Recursive Method\n3:- Recursive Method(Memo)\n4:- Exit")



# Execute the selected method
while True:
    # Accept user's choice
    print()
    choice = int(input("Enter Choice: "))
    if choice == 1:
        non_recursive_fib(n)

    elif choice == 2:
        print("\nRecursive Method: ")

        # Print Fibonacci series using recursion
        for i in range(n):
            print(recursive_fib(i), end="  ")

    elif choice == 3:
        print("\nRecursive Method (Memo): ")

        # Print Fibonacci series using memoization
        for i in range(n):
            print(recursive_fib_memo(i, memo=memo), end="  ")

    elif choice == 4:
        break  # Exit the program


#Sample Input:
#10
#1 (for Non Recursive)
#2 (for Recursive)
#3 (for Memoization Recursive)
#4 (for exit)