def return_nth_smallest_ascii(s):
    target_chars = s[62:84]
    return min(target_chars) if len(target_chars) >= 9 else None