def return_nth_smallest_ascii(s):
    if not s or len(s) < 5:
        return None
    chars_in_range = sorted(set(s[:5]))
    return chars_in_range[3] if len(chars_in_range) >= 4 else None