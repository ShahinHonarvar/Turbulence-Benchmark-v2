def filter_chars(input_string):
    altered_string = ''
    for idx, char in enumerate(input_string):
        if 23 <= idx <= 89 and 'w' <= char <= '{':
            continue
        altered_string += char
    return altered_string