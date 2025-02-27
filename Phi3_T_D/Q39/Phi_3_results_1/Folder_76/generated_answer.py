def return_n_greatest_chars(characters):
    return sorted(list(characters), key=ord, reverse=True)[:3]