def return_nth_smallest_ascii(s):
    within_range = s[12:56]
    smallest = sorted(set(within_range), key=lambda x: ord(x))[16]
    return smallest