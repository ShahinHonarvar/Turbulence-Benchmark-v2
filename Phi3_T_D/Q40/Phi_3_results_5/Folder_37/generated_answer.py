def return_n_smallest_chars(characters):
    return sorted(list(characters), key=ord, reverse=True)[:26]