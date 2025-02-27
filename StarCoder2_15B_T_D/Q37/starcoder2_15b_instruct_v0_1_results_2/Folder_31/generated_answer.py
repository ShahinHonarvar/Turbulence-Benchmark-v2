def filter_chars(string):
    return ''.join([char for char in string if (ord(char) < 57 or ord(char) > 96) or (char < '<' or char > 'w')])