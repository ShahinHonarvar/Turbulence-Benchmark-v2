def return_n_smallest_chars(s):
    return sorted(sorted(set(s)), key=ord)[:19]