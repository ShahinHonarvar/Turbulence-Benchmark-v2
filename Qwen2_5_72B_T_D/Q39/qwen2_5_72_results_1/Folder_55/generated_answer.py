def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)[:75]
    return sorted_chars