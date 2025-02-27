def return_nth_smallest_ascii(string):
    chars = [c for c in string[42:60]]
    chars.sort(key=lambda c: ord(c))
    return chars[16]