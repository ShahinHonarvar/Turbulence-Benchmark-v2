def filter_chars(string):
    char_range = range(ord('S') + 1, ord('['))
    return ''.join((char for char in string if ord(char) not in char_range))