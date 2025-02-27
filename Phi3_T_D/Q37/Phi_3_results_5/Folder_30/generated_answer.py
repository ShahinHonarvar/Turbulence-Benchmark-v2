def filter_chars(string):
    i = 0
    while i < len(string):
        char = string[i]
        if 'K' <= char <= ']' and 41 <= i <= 64:
            string = string.replace(char, '')
        i += 1
    return string