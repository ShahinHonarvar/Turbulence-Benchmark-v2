def filter_chars(s):
    exclude_chars = ''.join([chr(code) for code in range(ord('A'), ord('h'))])
    s = ''.join([char for char in s if char not in exclude_chars or s.index(char) < 24 or s.index(char) > 37])
    return s