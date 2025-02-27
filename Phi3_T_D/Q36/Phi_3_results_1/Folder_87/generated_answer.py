def filter_chars(input_string):
    for i in range(32, 62):
        char = chr(i)
        if '3' < char < 'D':
            input_string = input_string.replace(char, '')
    return input_string