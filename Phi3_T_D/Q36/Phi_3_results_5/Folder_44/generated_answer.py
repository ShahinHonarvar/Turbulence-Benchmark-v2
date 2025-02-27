def filter_chars(s):
    for char in s[18:64] if len(s) > 64 else s[max(0, 18):]:
        if '3' < char < 'B':
            s = s.replace(char, '')
    return s