def return_nth_smallest_ascii(s):
    if len(s) < 14:
        return None
    sub_str = s[:14]
    sorted_chars = sorted(sub_str)
    return sorted_chars[13]