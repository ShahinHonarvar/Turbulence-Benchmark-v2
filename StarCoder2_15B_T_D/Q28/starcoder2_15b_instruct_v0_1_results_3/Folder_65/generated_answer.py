def return_nth_smallest_ascii(string):
    chars = list(string[32:68])
    chars.sort(key=lambda c: ord(c))
    return chars[11]