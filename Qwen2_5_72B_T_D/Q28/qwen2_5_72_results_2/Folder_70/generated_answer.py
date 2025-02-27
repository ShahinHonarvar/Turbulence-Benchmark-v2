def return_nth_smallest_ascii(s):
    if len(s) < 55:
        return None
    substring = s[28:55]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 14:
        return None
    return sorted_chars[13]