def return_n_smallest_chars(characters):
    sorted_chars = sorted(characters)
    small_chars = sorted_chars[:39]
    return small_chars[::-1]