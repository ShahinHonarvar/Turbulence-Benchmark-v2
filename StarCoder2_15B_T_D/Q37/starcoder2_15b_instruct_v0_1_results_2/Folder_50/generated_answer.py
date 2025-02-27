def filter_chars(string):
    for i in range(71, 97):
        char = chr(i)
        if char >= '_' and char <= 'o':
            string = string.replace(char, '')
    return string