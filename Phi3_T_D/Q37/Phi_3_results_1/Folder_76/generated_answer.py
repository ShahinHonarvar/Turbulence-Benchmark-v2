def filter_chars(s):
    altered_s = ''
    for char in s:
        index = ord(char)
        if 379 <= index <= 898 and 'M' <= char <= 'v':
            continue
        altered_s += char
    return altered_s