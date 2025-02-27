def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[58:86] if s.count(c) == 1]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[18] if len(sorted_chars) > 18 else None