def return_n_greatest_chars(string):
    chars = list(string)
    sorted_chars = sorted(chars, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:66]