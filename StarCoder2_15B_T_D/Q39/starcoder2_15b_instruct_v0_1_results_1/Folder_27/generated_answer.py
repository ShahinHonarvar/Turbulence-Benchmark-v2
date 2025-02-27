def return_n_greatest_chars(string):
    chars = list(string)
    chars.sort(key=ord)
    chars.reverse()
    return chars[:82]