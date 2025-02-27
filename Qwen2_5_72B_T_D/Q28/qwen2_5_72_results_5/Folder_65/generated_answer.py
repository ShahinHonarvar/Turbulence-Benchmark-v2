def return_nth_smallest_ascii(s):
    relevant_chars = [c for c in s[32:68] if s.count(c) == 1]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[11] if len(sorted_chars) > 11 else None