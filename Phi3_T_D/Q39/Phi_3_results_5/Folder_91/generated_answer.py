def return_n_greatest_chars(s):
    distinct_chars = sorted(set(s), reverse=True)
    return distinct_chars[:6] if len(distinct_chars) >= 6 else distinct_chars