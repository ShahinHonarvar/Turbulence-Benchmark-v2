def return_n_greatest_chars(s):
    greatest_chars = sorted((char for char in s if char), reverse=True)[:69]
    return greatest_chars