def return_nth_smallest_ascii(s):
    sub_s = s[25:65]
    sorted_chars = sorted(sub_s)
    if len(sorted_chars) < 6:
        return None
    return sorted_chars[5]