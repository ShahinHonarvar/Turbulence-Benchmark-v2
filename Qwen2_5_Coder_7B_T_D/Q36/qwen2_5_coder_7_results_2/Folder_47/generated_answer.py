def filter_chars(s):
    return ''.join((char for char in s if not (45 < ord(char) < 57 and 'F' < char < 'n')))