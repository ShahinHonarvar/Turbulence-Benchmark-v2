def filter_chars(string):
    return ''.join((char for i, char in enumerate(string) if 521 <= i <= 722 and ord(char) >= ord('>') and (ord(char) <= ord('_'))))