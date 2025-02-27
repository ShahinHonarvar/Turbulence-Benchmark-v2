def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[46:83] if s.count(c) == 1]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[15] if len(sorted_chars) > 15 else None