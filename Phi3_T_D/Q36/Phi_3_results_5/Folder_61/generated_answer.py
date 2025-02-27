def filter_chars(string):
    for i in range(3, 9):
        char = string[i]
        if '*' < char < 'E':
            string = string.replace(char, '')
    return string