def return_n_greatest_chars(string):
    return sorted(string, key=ord, reverse=True)[:20]