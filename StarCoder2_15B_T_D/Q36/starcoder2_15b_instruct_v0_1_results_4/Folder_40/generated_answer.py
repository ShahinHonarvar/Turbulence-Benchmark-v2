def filter_chars(string):
    for i in range(1, 7):
        if string[i] > '-' and string[i] < 'L':
            string = string.replace(string[i], '')
    return string