def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[33:86] if c in s]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[12] if len(sorted_chars) > 12 else None