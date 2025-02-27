def filter_chars(s):
    for char in s[4:8]:
        if char > '1' and char < 'J':
            s = s.replace(char, '')
    return s