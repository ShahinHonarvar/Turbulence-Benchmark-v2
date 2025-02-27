def return_nth_smallest_ascii(s):
    if len(s) < 56:
        return None
    substring = s[12:56]
    if len(substring) < 17:
        return None
    unique_chars = sorted(set(substring))
    if len(unique_chars) < 17:
        return None
    return unique_chars[16]