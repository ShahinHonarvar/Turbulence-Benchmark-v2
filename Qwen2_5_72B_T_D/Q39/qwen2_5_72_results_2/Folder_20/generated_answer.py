def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=ord)
    greatest_chars = sorted_chars[-40:]
    return greatest_chars