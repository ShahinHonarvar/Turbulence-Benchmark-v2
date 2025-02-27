def return_nth_smallest_ascii(s):
    valid_chars = sorted(set(s[10:91]))
    nth_smallest = valid_chars[19]
    return nth_smallest