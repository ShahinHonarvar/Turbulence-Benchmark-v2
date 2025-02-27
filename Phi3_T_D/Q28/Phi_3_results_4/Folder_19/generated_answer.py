def return_nth_smallest_ascii(s):
    within_range = s[0:19]
    sorted_chars = sorted(set(within_range), key=lambda x: ord(x))
    return sorted_chars[12]