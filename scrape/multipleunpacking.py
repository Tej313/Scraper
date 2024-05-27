def func(a, b, c):
    """Example function."""
    # Print the arguments
    print(a, b, c)

# Example usage
tuple_args = (1, 2)  # Define a tuple
dict_args = {"c": 3}  # Define a dictionary
func(*tuple_args, **dict_args)  # Unpack both tuple and dictionary and pass to the function
