def filter_chars(s):
    return ''.join((char for char in s if (char < 'i' or char > 'k') or (20 > s.index(char) or s.index(char) > 62)))