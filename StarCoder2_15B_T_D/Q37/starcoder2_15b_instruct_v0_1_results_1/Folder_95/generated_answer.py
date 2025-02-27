def filter_chars(string):
    for char in string:
        if 35 <= ord(char) - ord(')') <= 6 and ')' <= char <= 'l':
            string = string.replace(char, '')
    return string