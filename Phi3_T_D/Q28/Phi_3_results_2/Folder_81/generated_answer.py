def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[:14]))
    if len(unique_chars) >= 14:
        return unique_chars[13]
    elif 14 - len(unique_chars) <= len(s) - 14:
        return s[len(unique_chars) + 13]
    else:
        raise ValueError('The string must contain at least 14 distinct characters within the first 14 indices.')