def filter_chars(input_str):
    for i in range(51, 78):
        char = input_str[i]
        if 'V' <= char <= 'Y':
            input_str = input_str.replace(char, '')
    return input_str