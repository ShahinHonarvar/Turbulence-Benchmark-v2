def return_n_greatest_chars(string):
    return sorted([char for char in string if ord(char) >= max((ord(c) for c in string)) - 62])