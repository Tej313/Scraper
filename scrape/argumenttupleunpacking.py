def sum_two_numbers(a, b):
    """Sum two numbers."""
    # Return the sum of a and b
    return a + b

# Example usage
numbers = (5, 10)  # Define a tuple of numbers
print(sum_two_numbers(*numbers))  # Unpack the tuple and pass to the function
