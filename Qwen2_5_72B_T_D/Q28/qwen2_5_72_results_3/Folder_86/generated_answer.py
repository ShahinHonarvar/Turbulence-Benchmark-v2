def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[44:70] if s.count(c) == 1]
    filtered_chars.sort(key=ord)
    return filtered_chars[14] if len(filtered_chars) > 14 else None