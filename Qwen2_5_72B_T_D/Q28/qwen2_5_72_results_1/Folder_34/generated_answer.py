def return_nth_smallest_ascii(s):
    sub_str = s[:19]
    sorted_chars = sorted(set(sub_str))
    if len(sorted_chars) >= 19:
        return sorted_chars[18]
    return None