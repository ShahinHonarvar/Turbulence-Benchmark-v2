def filter_chars(s):
    altered_s = ''
    for i, char in enumerate(s):
        if 35 <= i <= 89 and 'E' <= char <= 't':
            continue
        altered_s += char
    return altered_s