def filter_chars(string):
    return ''.join([char for char in string if char < '&' or char > 'v' or string.index(char) < 12 or (string.index(char) > 88)])