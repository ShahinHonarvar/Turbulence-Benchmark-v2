def return_nth_smallest_ascii(s):
    sub_str = s[51:79]
    if len(sub_str) < 9:
        return None
    sorted_chars = sorted(sub_str)
    return sorted_chars[8]