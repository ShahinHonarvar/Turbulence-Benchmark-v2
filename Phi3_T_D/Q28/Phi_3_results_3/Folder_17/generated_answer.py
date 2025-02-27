def return_nth_smallest_ascii(s):
    n = len(s)
    if n < 34:
        raise ValueError('Input string must contain at least 34 characters.')
    target_chars = sorted(s[4:33 + 1])
    return target_chars[3]