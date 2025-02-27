def filter_chars(s):
    altered_str = ''
    for i, char in enumerate(s[36:80]):
        if 'a' <= char <= 'i':
            continue
        altered_str += char
    return s[:36] + altered_str + s[80:]