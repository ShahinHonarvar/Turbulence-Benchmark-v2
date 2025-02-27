def return_nth_smallest_ascii(s):
    filtered_chars = sorted(s[1:47] if len(s) >= 47 else s[1:])
    return filtered_chars[12] if len(filtered_chars) >= 13 else None