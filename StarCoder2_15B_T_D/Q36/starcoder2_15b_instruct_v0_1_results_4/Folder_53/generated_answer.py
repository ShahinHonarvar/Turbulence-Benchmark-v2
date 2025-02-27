def filter_chars(string):
    for i in range(90, 97):
        char = chr(i)
        if char > 'j' and char < 'w':
            string = string.replace(char, '')
    return string