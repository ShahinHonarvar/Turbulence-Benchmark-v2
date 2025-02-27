def return_n_greatest_chars(chars):
    return sorted(list(chars), key=ord, reverse=True)[:19]