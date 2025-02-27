def return_nth_smallest_ascii(string):
    chars = [c for c in string[17:57]]
    chars.sort(key=lambda c: ord(c))
    return chars[8]