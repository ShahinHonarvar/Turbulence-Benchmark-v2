def filter_chars(string):
    for i in range(81, 86):
        char = string[i]
        if '!' < char < 's':
            string = string.replace(char, '')
    return string