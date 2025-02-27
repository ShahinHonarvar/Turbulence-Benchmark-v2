def filter_chars(s):
    return ''.join((char for index, char in enumerate(s) if (61 <= index <= 70 and ord('0') <= ord(char) <= ord('@')) == False))