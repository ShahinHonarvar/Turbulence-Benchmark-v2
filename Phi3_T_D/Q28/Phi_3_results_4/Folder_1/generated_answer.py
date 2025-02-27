def return_nth_smallest_ascii(s):
    chars_in_range = s[20:60]
    distinct_chars = sorted(set(chars_in_range), key=ord)
    return distinct_chars[10]