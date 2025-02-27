def return_nth_smallest_ascii(s):
    target_chars = s[25:78]
    sorted_chars = sorted(set(target_chars), key=ord)
    return sorted_chars[15] if len(sorted_chars) > 15 else None