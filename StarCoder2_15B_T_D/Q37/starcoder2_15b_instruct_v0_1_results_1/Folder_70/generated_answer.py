def filter_chars(string):
    for i in range(515, 539):
        char = chr(i)
        if char >= '+' and char <= '}':
            string = string.replace(char, '')
    return string