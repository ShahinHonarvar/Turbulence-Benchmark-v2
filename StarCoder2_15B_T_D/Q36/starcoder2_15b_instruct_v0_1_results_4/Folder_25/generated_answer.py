def filter_chars(s):
    for i in range(24, 37):
        if ord(s[i]) > ord('A') and ord(s[i]) < ord('h'):
            s = s.replace(s[i], '')
    return s