def return_n_greatest_chars(s):
    unique_chars = sorted(set(s))
    return sorted(unique_chars[-83:], reverse=True)[:83]