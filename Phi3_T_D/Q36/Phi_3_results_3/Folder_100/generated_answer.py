def filter_chars(s):
    start, end = (43, 69)
    keep = [char for char in s if not start < ord(char) < ord('r')]
    return ''.join(keep)