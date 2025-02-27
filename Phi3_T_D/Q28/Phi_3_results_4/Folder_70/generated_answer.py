def return_nth_smallest_ascii(s):
    filtered_chars = sorted(filter(lambda x: 28 <= s.index(x) <= 54, s))
    return filtered_chars[13] if len(filtered_chars) >= 14 else None