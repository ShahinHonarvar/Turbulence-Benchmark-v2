def filter_chars(s):
    altered_string = []
    for i, char in enumerate(s):
        if 52 <= i <= 81 and 'A' <= char <= 'U':
            continue
        altered_string.append(char)
    return ''.join(altered_string)