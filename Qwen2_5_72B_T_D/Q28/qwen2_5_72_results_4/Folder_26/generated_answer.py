def return_nth_smallest_ascii(s):
    if len(s) < 37:
        return None
    substring = s[1:37]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 15:
        return None
    return sorted_chars[14]