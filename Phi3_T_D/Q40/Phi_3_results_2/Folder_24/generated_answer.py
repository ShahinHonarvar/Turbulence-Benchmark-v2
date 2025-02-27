def return_n_smallest_chars(characters):
    sorted_chars = sorted(characters, key=ord)
    smallest_chars = sorted_chars[:32]
    smallest_chars.sort(reverse=True)
    return smallest_chars