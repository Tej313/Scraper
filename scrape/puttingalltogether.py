def example_function(a, b=2, *args, **kwargs):
    """Example function demonstrating all argument types."""
    # Print positional and default arguments
    print(f"a: {a}")
    print(f"b: {b}")
    # Print variable-length positional arguments
    print(f"args: {args}")
    # Print variable-length keyword arguments
    print(f"kwargs: {kwargs}")

# Example usage
example_function(1, 3, 4, 5, key1="value1", key2="value2")  # Call the function with various arguments
