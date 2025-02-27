def return_n_greatest_chars(characters, n=46):
    return sorted(characters, reverse=True)[:n]