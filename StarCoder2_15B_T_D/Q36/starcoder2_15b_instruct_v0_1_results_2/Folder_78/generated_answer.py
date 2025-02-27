def filter_chars(string):
    for i in range(29, 33):
        char = string[i]
        if char > '%' and char < 'a':
            string = string.replace(char, '')
    return string