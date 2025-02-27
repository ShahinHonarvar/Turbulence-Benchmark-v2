def return_n_smallest_chars(s):
    if len(s) < 20:
        return list(s)
    sorted_chars = sorted(s, key=ord)
    return sorted_chars[:20][::-1]