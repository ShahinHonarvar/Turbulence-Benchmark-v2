def return_nth_smallest_ascii(s):
    s_slice = s[30:71]
    unique_chars = sorted(set(s_slice))
    nth_smallest = unique_chars[14]
    return nth_smallest