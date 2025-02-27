def return_nth_smallest_ascii(s):
    if len(s) < 10:
        return None
    substring = s[9:23]
    sorted_chars = sorted(substring)
    return sorted_chars[3]