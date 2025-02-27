def filter_chars(s):
    for char in set(s[163:658]):
        if '(' < char < ']':
            s = s.replace(char, '')
    return s