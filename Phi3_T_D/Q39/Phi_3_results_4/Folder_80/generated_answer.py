def return_n_greatest_chars(s):
    greatest_chars = list(s)
    greatest_chars.sort(key=ord, reverse=True)
    return greatest_chars[:35]