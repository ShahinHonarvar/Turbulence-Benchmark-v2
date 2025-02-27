def return_nth_smallest_ascii(s):
    s = s[12:73]
    char = min(s, key=lambda c: ord(c))
    return char