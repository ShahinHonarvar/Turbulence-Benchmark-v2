def filter_chars(string):
    return ''.join((char for i, char in enumerate(string) if i < 44 or i >= 68 or (not (ord(char) > ord('W') and ord(char) < ord('x')))))