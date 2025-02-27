def return_nth_smallest_ascii(s):
    if len(s) < 70:
        return None
    substring = s[:70]
    sorted_chars = sorted(substring)
    return sorted_chars[9] if len(sorted_chars) > 9 else None