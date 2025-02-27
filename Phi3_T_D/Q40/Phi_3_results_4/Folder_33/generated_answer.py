def return_n_smallest_chars(characters):
    chars_sorted = sorted(characters)
    smallest_chars = chars_sorted[:36]
    smallest_chars.reverse()
    return smallest_chars