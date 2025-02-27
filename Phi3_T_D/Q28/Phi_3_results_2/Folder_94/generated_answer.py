def return_nth_smallest_ascii(s):
    target_segment = s[6:59]
    unique_chars = sorted(set(target_segment), key=ord)
    if len(unique_chars) >= 19:
        return unique_chars[18]
    else:
        return None