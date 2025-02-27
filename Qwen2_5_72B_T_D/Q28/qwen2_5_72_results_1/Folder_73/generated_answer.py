def return_nth_smallest_ascii(s):
    if len(s) < 70:
        return None
    substring = s[:70]
    sorted_chars = sorted(set(substring))
    if len(sorted_chars) < 10:
        return None
    return sorted_chars[9]