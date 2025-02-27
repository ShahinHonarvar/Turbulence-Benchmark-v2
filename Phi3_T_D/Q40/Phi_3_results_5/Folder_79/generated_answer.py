def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, reverse=True)[:82]
    sorted_chars.sort(reverse=False)
    return sorted_chars