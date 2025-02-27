def return_n_greatest_chars(s):
    chars = [char for char in s]
    chars.sort(key=ord, reverse=True)
    return chars[:6]