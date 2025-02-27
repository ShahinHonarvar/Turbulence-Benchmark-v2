def filter_chars(string):
    for i in range(587, 648):
        if string[i] > ',' and string[i] < 'c':
            string = string.replace(string[i], '')
    return string