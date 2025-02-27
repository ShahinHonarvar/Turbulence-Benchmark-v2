def return_n_greatest_chars(s):
    top_chars = sorted(s, reverse=True)[:85]
    return top_chars