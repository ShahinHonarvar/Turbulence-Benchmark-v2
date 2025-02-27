def return_nth_smallest_ascii(s):
    substring = s[:17]
    sorted_chars = sorted(substring)
    return sorted_chars[16] if len(sorted_chars) > 16 else None