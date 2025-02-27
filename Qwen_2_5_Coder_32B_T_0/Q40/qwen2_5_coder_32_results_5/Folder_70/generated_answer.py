def return_n_smallest_chars(s):
    return sorted([min(s, key=ord)], key=ord)[:2][::-1]