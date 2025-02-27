def filter_chars(s):
    return ''.join([char for char in s if not (81 < ord(char) < 86 and '!' < char < 's')])