def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=ord)
    greatest_chars = sorted_chars[-55:]
    return greatest_chars