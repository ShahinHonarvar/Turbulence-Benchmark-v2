def filter_chars(s):
    begin, end = (39, 87)
    for i in range(begin, end):
        char = s[i]
        if '!' < char < '}':
            s = s.replace(char, '')
    return s