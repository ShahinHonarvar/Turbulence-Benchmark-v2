def return_n_greatest_chars(input_string):
    sorted_chars = sorted(input_string, key=ord)
    greatest_chars = sorted_chars[-60:]
    return greatest_chars