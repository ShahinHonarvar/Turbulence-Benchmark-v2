def return_n_smallest_chars(s):
    distinct_chars = sorted(set(s))
    return sorted(distinct_chars)[:5] if len(distinct_chars) >= 5 else distinct_chars