def filter_chars(input_string):
    for ch in input_string[83:99 + 1]:
        if '*' <= ch <= 'j':
            input_string = input_string.replace(ch, '')
    return input_string