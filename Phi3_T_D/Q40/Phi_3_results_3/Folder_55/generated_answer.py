def return_n_smallest_chars(s):
    n = min(len(s), 75)
    result = sorted(s, key=ord)[:n][::-1]
    return result