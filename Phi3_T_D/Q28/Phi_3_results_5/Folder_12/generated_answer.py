def return_nth_smallest_ascii(s):
    target_chars = sorted(s[3:27])
    if len(target_chars) < 5:
        return None
    return target_chars[4]