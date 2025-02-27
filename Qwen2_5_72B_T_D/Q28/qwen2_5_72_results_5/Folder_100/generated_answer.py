def return_nth_smallest_ascii(s):
    if len(s) < 48:
        return None
    sub_str = s[5:48]
    sorted_chars = sorted(sub_str)
    if len(sorted_chars) < 13:
        return None
    return sorted_chars[12]