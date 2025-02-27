def filter_chars(s):
    modified_string = ''.join((char for i, char in enumerate(s) if not 46 < i < 68 or ord('H') <= ord(char) <= ord('s')))
    return modified_string