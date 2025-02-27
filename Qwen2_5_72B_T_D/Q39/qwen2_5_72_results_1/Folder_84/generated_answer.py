def return_n_greatest_chars(s):
    char_list = sorted(list(s))
    greatest_chars = char_list[-10:]
    return sorted(greatest_chars)