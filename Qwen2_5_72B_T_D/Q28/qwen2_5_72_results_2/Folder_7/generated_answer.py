def return_nth_smallest_ascii(s):
    substring = s[12:56]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 17:
        return None
    return sorted_chars[16]