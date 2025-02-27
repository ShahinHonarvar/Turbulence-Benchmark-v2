def filter_chars(s):
    for char in s[31:50]:
        if char > '/' and char < 'J':
            s = s.replace(char, '')
    return s