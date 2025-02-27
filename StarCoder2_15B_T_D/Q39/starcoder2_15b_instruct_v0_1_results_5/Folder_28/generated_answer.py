def return_n_greatest_chars(string):
    chars = [c for c in string]
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[-3:]