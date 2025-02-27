def filter_chars(string):
    start, end = (81, 86)
    for i in range(start, end):
        char = string[i]
        if '!' < char < 's':
            string = string.replace(char, '')
    return string