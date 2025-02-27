def return_n_smallest_chars(s):
    return sorted([min(s, key=ord), min(s.replace(min(s, key=ord), ''), key=ord)], reverse=True)