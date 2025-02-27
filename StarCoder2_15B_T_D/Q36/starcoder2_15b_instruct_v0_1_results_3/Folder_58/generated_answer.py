def filter_chars(string):
    return ''.join([c for c in string if ord(c) <= ord('B') or ord(c) >= ord('z')])