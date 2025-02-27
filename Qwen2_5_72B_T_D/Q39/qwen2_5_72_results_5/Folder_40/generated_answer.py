def return_n_greatest_chars(s):
    chars_list = list(s)
    chars_list.sort(reverse=True)
    return chars_list[:7]