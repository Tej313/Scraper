def demo_function(a, b, c=10, *args, **kwargs):
    print(a, b, c)
    print(args)
    print(kwargs)

# Example usage
demo_function(1, 2, 3, 4, 5, key1="value1", key2="value2")
