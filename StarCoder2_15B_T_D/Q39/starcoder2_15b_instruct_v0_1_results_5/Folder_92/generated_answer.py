def return_n_greatest_chars(string):
    chars = list(string)
    chars.sort(key=lambda c: ord(c), reverse=True)
    return sorted(chars[:63])