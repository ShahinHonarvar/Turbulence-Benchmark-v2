def return_nth_smallest_ascii(s):
    filtered_chars = [s[i] for i in range(46, min(83, len(s))) if s[i] in s[46:83]]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[15] if len(sorted_chars) > 15 else None