def return_nth_smallest_ascii(s):
    sub_str = s[9:23]
    sorted_chars = sorted(set(sub_str))
    return sorted_chars[3]