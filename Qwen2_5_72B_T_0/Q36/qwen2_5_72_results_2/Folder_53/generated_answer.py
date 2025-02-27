def filter_chars(s):
    result = ''.join([char for char in s if not (90 < ord(char) < 97 and 'j' < char < 'w')])
    return result