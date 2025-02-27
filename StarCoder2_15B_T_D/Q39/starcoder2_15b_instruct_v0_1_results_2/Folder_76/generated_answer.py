def return_n_greatest_chars(string):
    chars = list(string)
    chars.sort(key=lambda x: ord(x), reverse=True)
    return chars[:3]