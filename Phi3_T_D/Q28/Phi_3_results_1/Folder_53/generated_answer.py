def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[40:61])
    return sorted_chars[18] if len(sorted_chars) >= 19 else None