def return_n_greatest_chars(string):
    sorted_str = sorted(string, key=lambda c: ord(c), reverse=True)
    return sorted_str[:61]