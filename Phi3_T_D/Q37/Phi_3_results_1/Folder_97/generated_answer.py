def filter_chars(input_string):
    start, end = (227, 235)
    for i in range(start, end + 1):
        char = input_string[i]
        if 'D' <= char <= 'u':
            input_string = input_string.replace(char, '')
    return input_string