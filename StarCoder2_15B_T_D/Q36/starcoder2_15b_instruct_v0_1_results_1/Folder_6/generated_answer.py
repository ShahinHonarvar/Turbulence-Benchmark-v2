def filter_chars(string):
    for i, char in enumerate(string):
        if 31 < i < 70 and char > 'B' and (char < 'v'):
            string = string.replace(char, '')
    return string