def return_n_smallest_chars(s):
    if len(s) < 54:
        return sorted(s)
    else:
        return sorted(s)[:54][::-1]