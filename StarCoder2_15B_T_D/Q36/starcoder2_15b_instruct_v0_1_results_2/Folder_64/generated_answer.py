def filter_chars(string):
    for i in range(1, 7):
        char = string[i]
        if char > '3' and char < '^':
            string = string.replace(char, '')
    return string