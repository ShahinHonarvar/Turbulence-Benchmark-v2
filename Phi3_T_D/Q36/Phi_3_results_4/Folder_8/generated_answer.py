def filter_chars(s):
    string_length = len(s)
    if string_length > 93:
        sub_string = s[82:93]
        for char in sub_string:
            if ord('!') < ord(char) < ord('*'):
                s = s.replace(char, '')
    return s