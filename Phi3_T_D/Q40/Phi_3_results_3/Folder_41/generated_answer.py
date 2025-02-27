def return_n_smallest_chars(s):
    if len(s) > 37:
        s = ''.join(sorted(s)[:37])
    else:
        s = ''.join(sorted(s))
    return list(s)