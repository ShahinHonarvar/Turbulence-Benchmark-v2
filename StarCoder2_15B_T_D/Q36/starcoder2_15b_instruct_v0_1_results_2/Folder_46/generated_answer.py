def filter_chars(string):
    for i in range(19, 69):
        if string[i] > '<' and string[i] < 'C':
            string = string.replace(string[i], '')
    return string