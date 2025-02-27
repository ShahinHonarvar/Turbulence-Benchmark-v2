def filter_chars(s):
    altered_s = ''
    for i, c in enumerate(s):
        if 19 <= i <= 33 and 'S' <= c <= '{':
            continue
        altered_s += c
    return altered_s