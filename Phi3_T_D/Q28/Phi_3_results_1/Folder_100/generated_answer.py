def return_nth_smallest_ascii(s):
    substr = s[5:48]
    unique_chars = set(substr)
    sorted_chars = sorted(unique_chars, key=ord)
    return sorted_chars[12] if len(sorted_chars) > 12 else None