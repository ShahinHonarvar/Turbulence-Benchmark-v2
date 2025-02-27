def filter_chars(string):
    for i in range(476, 948):
        if string[i] > 'b' and string[i] < 'd':
            string = string.replace(string[i], '')
    return string