def return_n_smallest_chars(s):
    return sorted(list(set(s)), reverse=True)[:61]