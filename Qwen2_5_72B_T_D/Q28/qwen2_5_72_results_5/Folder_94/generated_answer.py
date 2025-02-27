def return_nth_smallest_ascii(s):
    substring = s[6:59]
    if len(substring) < 19:
        return None
    sorted_chars = sorted(substring)
    return sorted_chars[18]