def return_n_greatest_chars(str):
    chars = list(str)
    sorted_chars = sorted(chars, key=lambda x: ord(x), reverse=True)
    return sorted_chars[:83]