def return_nth_smallest_ascii(s):
    valid_chars = s[12:88]
    if len(valid_chars) < 17:
        return None
    sorted_chars = sorted(set(valid_chars))
    return sorted_chars[16] if len(sorted_chars) > 16 else None