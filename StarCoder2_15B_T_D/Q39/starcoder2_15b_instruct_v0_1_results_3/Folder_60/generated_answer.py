def return_n_greatest_chars(string):
    chars = sorted(string, key=lambda c: ord(c), reverse=True)
    return sorted(chars[:28])