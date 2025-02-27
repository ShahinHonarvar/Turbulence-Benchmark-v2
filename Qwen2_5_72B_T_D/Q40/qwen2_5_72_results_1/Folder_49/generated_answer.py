def return_n_smallest_chars(s):
    return sorted([char for char in sorted(s)][:76], reverse=True)