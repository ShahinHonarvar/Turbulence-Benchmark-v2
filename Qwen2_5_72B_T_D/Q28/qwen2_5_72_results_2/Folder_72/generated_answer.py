def return_nth_smallest_ascii(s):
    relevant_chars = [c for c in s[33:61] if s.count(c) == 1]
    sorted_chars = sorted(relevant_chars, key=ord)
    return sorted_chars[17] if len(sorted_chars) > 17 else None