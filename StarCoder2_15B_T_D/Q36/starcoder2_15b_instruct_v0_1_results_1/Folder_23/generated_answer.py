def filter_chars(s):
    for ch in s[21:25]:
        if ord(ch) > ord('5') and ord(ch) < ord('}'):
            s = s.replace(ch, '')
    return s