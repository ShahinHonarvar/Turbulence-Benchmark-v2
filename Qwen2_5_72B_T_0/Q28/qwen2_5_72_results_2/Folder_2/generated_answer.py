def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[48:77] if s.count(c) == 1]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[4] if len(sorted_chars) > 4 else None