def return_n_smallest_chars(s):
    s = sorted(s, key=ord)
    result = s[:26]
    return sorted(result, reverse=True)