def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)[:65]
    return sorted(sorted_chars, reverse=True)