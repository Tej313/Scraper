def modify_dict(d):
    """Add a key-value pair to the dictionary."""
    d["new_key"] = "new_value"

my_dict = {"original_key": "original_value"}
modify_dict(my_dict)

# The original dictionary is modified
print(my_dict)  # Output: {'original_key': 'original_value', 'new_key': 'new_value'}
