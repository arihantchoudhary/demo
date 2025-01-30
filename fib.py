def fibonacci_series(n):
    """Generate a Fibonacci series up to n terms."""
    if n <= 0:
        return "Please enter a positive integer."
    
    fib_series = [0, 1]  # Initialize with first two numbers
    
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])  # Sum of last two numbers
    
    return fib_series[:n]  # Return only up to n terms

# Example usage
num_terms = 10
print(fibonacci_series(num_terms))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
