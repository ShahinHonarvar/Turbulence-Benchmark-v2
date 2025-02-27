def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)[:76]
    return sorted_chars