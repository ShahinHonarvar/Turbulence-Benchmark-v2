def filter_chars(string):
    for i in range(49, 56):
        char = chr(i)
        if char > 'I' and char < 'a':
            string = string.replace(char, '')
    return string