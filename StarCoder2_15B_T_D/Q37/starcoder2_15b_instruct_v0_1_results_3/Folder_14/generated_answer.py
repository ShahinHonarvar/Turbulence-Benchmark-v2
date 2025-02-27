def filter_chars(string):
    return ''.join([c for c in string if c < 'A' or c > 'b' or (ord(c) < 35 or ord(c) > 98)])