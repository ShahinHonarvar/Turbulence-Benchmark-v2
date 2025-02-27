def return_nth_smallest_ascii(s):
    chars = [c for c in s[33:61]]
    chars.sort(key=lambda c: ord(c))
    return chars[17]