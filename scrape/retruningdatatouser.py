def divide(a, b):
    """Divide a by b and return the quotient and remainder."""
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# Example usage
q, r = divide(10, 3)
print(f"Quotient: {q}, Remainder: {r}")
