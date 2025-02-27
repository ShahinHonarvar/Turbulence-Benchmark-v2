def filter_chars(s):
    for c in s[26:80]:
        if ord(c) > ord('<') and ord(c) < ord('>'):
            s = s.replace(c, '')
    return s