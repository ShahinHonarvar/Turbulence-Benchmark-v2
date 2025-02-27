def return_nth_smallest_ascii(s):
    if len(s) < 22:
        return None
    substring = s[15:22]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 6:
        return None
    return sorted_chars[5]