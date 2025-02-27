def return_n_smallest_chars(s):
    result = sorted(s, key=ord)[:76]
    return result