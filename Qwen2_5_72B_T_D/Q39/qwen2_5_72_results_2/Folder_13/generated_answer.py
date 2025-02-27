def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=ord)
    greatest_chars = sorted_chars[-31:]
    return greatest_chars