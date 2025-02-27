def return_n_greatest_chars(s):
    sorted_list = sorted(s, reverse=True)[:64]
    return sorted_list