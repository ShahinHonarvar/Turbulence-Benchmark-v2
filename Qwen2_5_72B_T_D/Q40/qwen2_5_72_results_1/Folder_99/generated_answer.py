def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)[:35]
    return sorted(sorted_chars, key=ord, reverse=True)