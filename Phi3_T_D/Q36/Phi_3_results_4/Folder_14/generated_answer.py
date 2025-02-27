def filter_chars(s):
    altered_str = ''
    for i, char in enumerate(s):
        if 41 < i < 56:
            if 'a' <= char <= 'Z' or 'A' <= char <= 'z':
                continue
        altered_str += char
    return altered_str