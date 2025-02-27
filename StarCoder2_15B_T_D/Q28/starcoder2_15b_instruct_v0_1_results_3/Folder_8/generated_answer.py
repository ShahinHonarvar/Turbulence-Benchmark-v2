def return_nth_smallest_ascii(string):
    chars = [c for c in string if 60 <= string.index(c) <= 88]
    chars.sort(key=lambda c: ord(c))
    return chars[6]