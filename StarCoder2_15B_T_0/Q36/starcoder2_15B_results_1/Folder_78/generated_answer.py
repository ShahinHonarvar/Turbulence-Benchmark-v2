def filter_chars(string):
    for i in range(29, 33):
        if string[i] > '%' and string[i] < 'a':
            string = string.replace(string[i], '')
    return string