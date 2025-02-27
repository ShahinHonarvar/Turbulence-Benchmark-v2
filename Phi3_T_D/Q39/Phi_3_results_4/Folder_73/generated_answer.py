def return_n_greatest_chars(chars):
    sorted_list = sorted(chars, reverse=True)[:80]
    return sorted_list