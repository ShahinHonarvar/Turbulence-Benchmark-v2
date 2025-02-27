def return_nth_smallest_ascii(s):
    if len(s) < 84:
        return None
    sub_str = s[17:84]
    sorted_chars = sorted(sub_str)
    return sorted_chars[4]