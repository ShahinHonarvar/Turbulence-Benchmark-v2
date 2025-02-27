def return_nth_smallest_ascii(s):
    sub_str = s[25:78]
    sorted_chars = sorted(set(sub_str))
    if len(sorted_chars) >= 16:
        return sorted_chars[15]
    return None