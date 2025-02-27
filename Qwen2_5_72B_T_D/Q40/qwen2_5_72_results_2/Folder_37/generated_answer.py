def return_n_smallest_chars(s):
    s = sorted(s, key=ord)
    s = s[:26]
    return sorted(s, reverse=True)