def return_nth_smallest_ascii(s):
    chars = [c for c in s[38:65]]
    chars.sort(key=lambda c: ord(c))
    return chars[13]