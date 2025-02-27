def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[33:86] if s.count(c) == 1]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[12] if len(sorted_chars) > 12 else None