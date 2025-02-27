def filter_chars(string):
    return ''.join((char for char in string if (char < 'S' or char > 's') or not 41 <= string.index(char) <= 86))