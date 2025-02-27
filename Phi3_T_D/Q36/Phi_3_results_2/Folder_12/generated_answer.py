def filter_chars(s):
    return ''.join([char for char in s if not (32 < ord(char) < 84 and 'm' < char < 'w')])