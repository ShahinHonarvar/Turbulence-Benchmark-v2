def return_n_greatest_chars(string):
    return sorted(list(string), key=ord, reverse=True)[:52]