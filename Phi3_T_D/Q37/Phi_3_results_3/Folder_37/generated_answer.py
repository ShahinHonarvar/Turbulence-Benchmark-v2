def filter_chars(s):
    modified_s = ''
    for i, char in enumerate(s, 1):
        if 17 <= i <= 63 and 'O' <= char <= '^':
            continue
        modified_s += char
    return modified_s