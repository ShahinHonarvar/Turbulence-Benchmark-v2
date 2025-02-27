def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)[:32]
    return sorted_chars