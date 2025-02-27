def return_nth_smallest_ascii(s):
    substring = s[34:82]
    unique_chars = sorted(set(substring))
    return unique_chars[11] if len(unique_chars) > 11 else None