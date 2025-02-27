def return_n_greatest_chars(string):
    greatest_chars = sorted([char for char in string], reverse=True)[:12]
    return greatest_chars