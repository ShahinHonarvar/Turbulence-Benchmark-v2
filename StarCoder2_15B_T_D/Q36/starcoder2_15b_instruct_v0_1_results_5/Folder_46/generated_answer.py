def filter_chars(string):
    return ''.join([char for char in string if not (ord(char) > ord('<') and ord(char) < ord('C'))])