def filter_chars(s):
    altered_str = ''
    for i, char in enumerate(s, 1):
        if 513 <= i <= 877 and '?' <= char <= 'n':
            continue
        altered_str += char
    return altered_str