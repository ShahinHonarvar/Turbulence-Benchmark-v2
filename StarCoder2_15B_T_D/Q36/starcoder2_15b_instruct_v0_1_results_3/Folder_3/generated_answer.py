def filter_chars(string):
    return ''.join((char for char in string if not (42 < string.index(char) < 78 and '!' < char < '?')))