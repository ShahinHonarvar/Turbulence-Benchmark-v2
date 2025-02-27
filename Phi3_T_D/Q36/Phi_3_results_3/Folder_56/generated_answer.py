def filter_chars(string):
    result = []
    for index, char in enumerate(string[31:50]):
        if '/' < char < 'J':
            string = string.replace(char, '')
    return string