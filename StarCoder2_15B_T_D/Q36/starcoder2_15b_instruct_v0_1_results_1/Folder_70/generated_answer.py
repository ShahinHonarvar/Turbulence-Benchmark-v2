def filter_chars(string):
    for i in range(170, 195):
        if '!' < string[i] < '}':
            string = string[:i] + string[i + 1:]
    return string