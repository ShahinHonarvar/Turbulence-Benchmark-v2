def return_n_smallest_chars(s):
    return sorted(sorted(s, key=ord)[:6], reverse=True)