def filter_chars(s):
    target_char = '7'
    altered_string = ''
    for i, character in enumerate(s):
        if 4 <= i <= 4 and '7' <= character <= 'o':
            continue
        altered_string += character
    return altered_string