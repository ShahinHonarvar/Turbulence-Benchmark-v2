def filter_chars(string):
    for i in range(45, 57):
        char = chr(i)
        string = string.replace(char, '')
    return string