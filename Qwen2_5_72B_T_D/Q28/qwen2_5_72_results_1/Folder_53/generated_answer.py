def return_nth_smallest_ascii(s):
    substring = s[40:61]
    unique_chars = set(substring)
    sorted_chars = sorted(unique_chars)
    if len(sorted_chars) < 19:
        return None
    return sorted_chars[18]