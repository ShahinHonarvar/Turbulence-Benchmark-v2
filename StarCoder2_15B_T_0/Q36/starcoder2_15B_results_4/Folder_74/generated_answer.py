def filter_chars(string):
    for i in range(33, 36):
        char = chr(i)
        if char > '>' and char < 'A':
            string = string.replace(char, '')
    return string