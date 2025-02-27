def return_n_greatest_chars(string):
    return sorted([c for c in string], reverse=True)[:29]