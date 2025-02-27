def return_n_greatest_chars(s):
    greatest_chars = sorted(s)[-24:]
    return sorted(greatest_chars, reverse=True)