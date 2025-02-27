def return_nth_smallest_ascii(s):
    substring = s[28:55]
    unique_chars = sorted(set(substring))
    if len(unique_chars) < 14:
        return None
    return unique_chars[13]