def return_n_greatest_chars(s):
    chars = list(s)
    chars.sort(key=ord)
    chars.reverse()
    return chars[:47]