def filter_chars(string):
    for i in range(66, 90):
        char = chr(i)
        if char > '#' and char < 'T':
            string = string.replace(char, '')
    return string