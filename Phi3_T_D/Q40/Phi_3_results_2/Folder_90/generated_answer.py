def return_n_smallest_chars(s):
    distinct_chars = sorted(set(s))
    if len(distinct_chars) > 24:
        return list(reversed(distinct_chars[:24]))
    else:
        return list(reversed(distinct_chars))