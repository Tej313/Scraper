def modify_list(my_list):
    """Append a value to the list."""
    my_list.append(4)

original_list = [1, 2, 3]
modify_list(original_list)

# The original list is modified
print(original_list)  # Output: [1, 2, 3, 4]
