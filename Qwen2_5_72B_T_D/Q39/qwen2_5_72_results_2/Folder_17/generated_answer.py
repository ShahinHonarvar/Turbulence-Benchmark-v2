def return_n_greatest_chars(s):
    char_list = sorted(s)
    greatest_chars = char_list[-11:]
    return greatest_chars