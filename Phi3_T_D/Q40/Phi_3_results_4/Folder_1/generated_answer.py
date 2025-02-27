def return_n_smallest_chars(s):
    if len(s) < 11:
        return list(s)[::-1]
    else:
        return sorted(s)[-11:][::-1]