def return_n_greatest_chars(str):
    sorted_chars = sorted(str, key=lambda char: -ord(char))
    return sorted_chars[:48]