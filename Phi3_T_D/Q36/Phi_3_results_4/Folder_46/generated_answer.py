def filter_chars(string):
    new_string = ''
    for i in range(19, 69):
        char = string[i]
        if '<' < char < 'C':
            string = string.replace(char, '')
    return string