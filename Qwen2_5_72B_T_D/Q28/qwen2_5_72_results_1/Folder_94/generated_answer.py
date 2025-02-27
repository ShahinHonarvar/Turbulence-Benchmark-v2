def return_nth_smallest_ascii(s):
    substring = s[6:59]
    unique_chars = sorted(set(substring))
    if len(unique_chars) >= 19:
        return unique_chars[18]
    return None