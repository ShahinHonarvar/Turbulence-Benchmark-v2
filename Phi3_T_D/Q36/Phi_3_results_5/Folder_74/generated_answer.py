def filter_chars(string):
    for char in range(33, 36):
        char = chr(char)
        if '>' < char < 'A':
            string = string.replace(char, '')
    return string