def filter_chars(string):
    for i in range(69, 97):
        char = chr(i)
        if char > 'V' and char < 'j':
            string = string.replace(char, '')
    return string