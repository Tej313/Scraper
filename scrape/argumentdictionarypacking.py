def display_info(**kwargs):
    """Display information."""
    for key, value in kwargs.items():
        # Print each key-value pair
        print(f"{key}: {value}")

# Example usage
display_info(name="Alice", age=30, city="New York")  # Call the function with keyword arguments
