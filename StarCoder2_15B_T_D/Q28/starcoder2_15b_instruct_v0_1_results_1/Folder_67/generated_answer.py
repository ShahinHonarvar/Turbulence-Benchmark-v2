def return_nth_smallest_ascii(string):
    chars = [c for c in string[60:84]]
    chars.sort(key=lambda c: ord(c))
    return chars[13]