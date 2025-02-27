def return_n_greatest_chars(string):
    return sorted([c for c in string if string.count(c) == 1], key=ord, reverse=True)[:38]