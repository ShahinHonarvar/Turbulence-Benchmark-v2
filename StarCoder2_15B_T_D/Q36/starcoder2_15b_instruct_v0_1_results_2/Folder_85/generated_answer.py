def filter_chars(string):
    return ''.join((char for i, char in enumerate(string) if i < 55 or i >= 80 or (not (ord(char) > ord('S') and ord(char) < ord('s')))))