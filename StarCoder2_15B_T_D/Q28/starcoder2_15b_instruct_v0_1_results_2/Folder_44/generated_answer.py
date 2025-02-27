def return_nth_smallest_ascii(s):
    chars = [c for c in s[20:31]]
    chars.sort(key=ord)
    return chars[7]