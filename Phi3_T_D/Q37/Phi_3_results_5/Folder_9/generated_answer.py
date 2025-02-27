def filter_chars(s):
    altered_s = []
    for i, char in enumerate(s):
        if 38 <= i <= 99 and 'A' <= char <= 'Q':
            continue
        altered_s.append(char)
    return ''.join(altered_s)