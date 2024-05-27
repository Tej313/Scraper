def outer_function():
    outer_var = "outer"

    def inner_function():
        inner_var = "inner"
        print(outer_var)  # Accessing outer function variable

    inner_function()
    # print(inner_var)  # This would raise a NameError

outer_function()
