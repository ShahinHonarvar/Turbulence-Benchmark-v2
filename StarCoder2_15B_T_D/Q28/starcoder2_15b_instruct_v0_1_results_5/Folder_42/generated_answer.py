def return_nth_smallest_ascii(string):
    chars = [c for c in string[12:73]]
    chars.sort(key=lambda c: ord(c))
    return chars[12]