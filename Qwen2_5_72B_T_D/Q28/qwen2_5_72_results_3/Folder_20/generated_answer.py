def return_nth_smallest_ascii(s):
    if len(s) < 65:
        return None
    substring = s[25:65]
    if len(substring) < 6:
        return None
    unique_chars = sorted(set(substring))
    if len(unique_chars) < 6:
        return None
    return unique_chars[5]