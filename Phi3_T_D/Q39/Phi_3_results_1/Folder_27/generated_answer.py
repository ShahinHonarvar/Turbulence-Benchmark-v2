def return_n_greatest_chars(s):
    if len(s) < 82 or len(set(s)) != len(s):
        return 'Input string must contain at least 82 distinct characters.'
    sorted_chars = sorted(set(s), reverse=True)
    return sorted_chars[:82]