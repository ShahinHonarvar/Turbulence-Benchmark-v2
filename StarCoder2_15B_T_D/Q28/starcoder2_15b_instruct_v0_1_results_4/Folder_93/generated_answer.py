def return_nth_smallest_ascii(s):
    chars = [c for c in s[42:60]]
    chars.sort(key=lambda c: ord(c))
    return chars[16]