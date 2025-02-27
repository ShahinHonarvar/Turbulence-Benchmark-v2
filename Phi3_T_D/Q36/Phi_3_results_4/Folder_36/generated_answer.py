def filter_chars(string):
    target_range = string[283:484]
    for char in target_range:
        if 'l' < char < 't':
            string = string.replace(char, '')
    return string