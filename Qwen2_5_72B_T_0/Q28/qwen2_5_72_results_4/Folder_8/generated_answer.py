def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[60:89] if s.count(c) == 1]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[6] if len(sorted_chars) > 6 else None