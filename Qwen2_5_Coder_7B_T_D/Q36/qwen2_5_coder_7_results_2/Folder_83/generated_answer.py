def filter_chars(s):
    return ''.join((char for char in s if not (72 < ord(char) < 93 and '<' < char < 'J')))