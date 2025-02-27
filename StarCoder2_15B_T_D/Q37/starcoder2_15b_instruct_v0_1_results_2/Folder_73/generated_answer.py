def filter_chars(string):
    keep_chars = [char for char in string if char < '7' or char > 'e' or 22 > string.index(char) or (string.index(char) > 85)]
    return ''.join(keep_chars)