def return_n_greatest_chars(s):
    highest_chars = sorted(s, reverse=True)[:9]
    return highest_chars