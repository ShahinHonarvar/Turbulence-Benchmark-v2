def return_n_greatest_chars(s):
    greatest_chars = sorted([char for char in s], reverse=True)[:73]
    return greatest_chars