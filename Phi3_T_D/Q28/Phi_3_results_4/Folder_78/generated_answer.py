def return_nth_smallest_ascii(s):
    filtered_chars = sorted(set(s[0:88]))
    nth_smallest = filtered_chars[13]
    return nth_smallest