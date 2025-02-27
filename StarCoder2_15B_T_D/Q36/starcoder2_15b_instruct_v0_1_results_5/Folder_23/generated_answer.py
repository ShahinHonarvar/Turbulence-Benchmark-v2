def filter_chars(string):
    for char in string[21:25]:
        if char > '5' and char < '}':
            string = string.replace(char, '')
    return string