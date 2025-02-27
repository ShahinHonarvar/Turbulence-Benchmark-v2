def filter_chars(s):
    altered_string = ''
    for i, char in enumerate(s):
        if 35 <= i <= 51 and 'H' <= char <= 's':
            continue
        altered_string += char
    return altered_string