def filter_chars(string):
    for index, char in enumerate(string):
        if 54 <= index <= 62 and ord(')') <= ord(char) <= ord('9'):
            string = string.replace(char, '')
    return string