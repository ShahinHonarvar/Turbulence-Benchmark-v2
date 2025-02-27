def return_nth_smallest_ascii(s):
    start, end = (63, 76)
    target_chars = sorted(set(s[start:end + 1]))
    if len(target_chars) < 14:
        return None
    return target_chars[13]