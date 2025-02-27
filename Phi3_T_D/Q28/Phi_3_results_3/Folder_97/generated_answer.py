def return_nth_smallest_ascii(s):
    target_chars = s[15:22]
    distinct_chars = sorted(set(target_chars))
    nth_smallest = distinct_chars[5]
    return nth_smallest