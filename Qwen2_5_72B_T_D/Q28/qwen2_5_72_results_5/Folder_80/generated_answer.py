def return_nth_smallest_ascii(s):
    substring = s[51:90]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 14:
        return None
    return sorted_chars[13]