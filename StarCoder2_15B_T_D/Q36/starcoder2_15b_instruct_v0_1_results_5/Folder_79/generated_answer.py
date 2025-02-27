def filter_chars(string):
    for char in string[11:46]:
        if '!' < char < 'A':
            string = string.replace(char, '')
    return string