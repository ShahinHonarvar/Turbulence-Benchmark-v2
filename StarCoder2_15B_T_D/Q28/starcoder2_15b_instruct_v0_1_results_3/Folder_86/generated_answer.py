def return_nth_smallest_ascii(s):
    chars = [c for c in s[44:70]]
    chars.sort(key=lambda c: ord(c))
    return chars[14]