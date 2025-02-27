def return_nth_smallest_ascii(s):
    substring = s[6:59]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 19:
        return sorted_chars[18]
    return None