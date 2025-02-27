def return_n_smallest_chars(chars):
    chars_sorted = sorted(chars, key=ord)
    return chars_sorted[:47][::-1]