def return_n_greatest_chars(string):
    greatest_chars = sorted(string)[-28:]
    return sorted(greatest_chars)