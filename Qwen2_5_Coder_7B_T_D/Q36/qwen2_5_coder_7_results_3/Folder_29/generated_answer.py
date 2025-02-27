def filter_chars(s):
    return ''.join([char for char in s if not (46 < ord(char) < 68 and 'H' < char < 's')])