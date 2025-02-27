def return_nth_smallest_ascii(s):
    substring = s[5:90]
    unique_chars = set(substring)
    sorted_chars = sorted(unique_chars)
    return sorted_chars[12] if len(sorted_chars) > 12 else None