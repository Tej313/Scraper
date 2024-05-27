def append_to_list(value, my_list=[]):
    """Append a value to a list."""
    my_list.append(value)
    return my_list

# Example usage
list1 = append_to_list(1)
list2 = append_to_list(2)

# Both lists share the same default list object
print(list1)  # Output: [1, 2]
print(list2)  # Output: [1, 2]
