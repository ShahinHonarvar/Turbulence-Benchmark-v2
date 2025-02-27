def return_nth_smallest_ascii(s):
    target_chars = s[58:86]
    sorted_chars = sorted(target_chars, key=ord)
    return sorted_chars[18] if len(sorted_chars) >= 19 else None