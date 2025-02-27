def return_n_smallest_chars(chars):
    sorted_characters = sorted(chars)
    return sorted_characters[:3][::-1]