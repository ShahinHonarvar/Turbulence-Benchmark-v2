def filter_chars(s):
    t = ''.join(s[163:658])
    for char in set(t):
        if '(' < char < ']':
            s = s.replace(char, '')
    return s