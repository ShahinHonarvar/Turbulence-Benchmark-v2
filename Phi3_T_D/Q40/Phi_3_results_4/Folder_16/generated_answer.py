def return_n_smallest_chars(characters):
    sorted_chars = sorted(characters, reverse=True)
    return sorted_chars[:64]