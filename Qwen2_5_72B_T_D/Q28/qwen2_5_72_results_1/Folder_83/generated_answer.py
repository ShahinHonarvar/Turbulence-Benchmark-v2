def return_nth_smallest_ascii(s):
    if len(s) < 71:
        return None
    substring = s[30:71]
    unique_chars = set(substring)
    sorted_chars = sorted(unique_chars)
    if len(sorted_chars) < 15:
        return None
    return sorted_chars[14]