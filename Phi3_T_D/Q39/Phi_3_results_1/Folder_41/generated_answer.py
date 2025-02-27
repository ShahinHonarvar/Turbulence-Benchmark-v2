def return_n_greatest_chars(string):
    max_chars = sorted(string)[-37:]
    return sorted(max_chars, reverse=True)