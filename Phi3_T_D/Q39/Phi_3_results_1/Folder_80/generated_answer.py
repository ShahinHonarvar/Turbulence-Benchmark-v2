def return_n_greatest_chars(s):
    return sorted(sorted(list(s))[::-1][:35])[::-1]