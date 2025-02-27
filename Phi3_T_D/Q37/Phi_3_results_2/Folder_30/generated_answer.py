def filter_chars(s):
    altered_str = ''
    for i, char in enumerate(s):
        if 41 <= i <= 64 and 'K' <= char <= ']':
            continue
        altered_str += char
    return altered_str