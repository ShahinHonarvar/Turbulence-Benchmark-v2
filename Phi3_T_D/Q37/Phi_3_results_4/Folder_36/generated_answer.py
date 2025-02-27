def filter_chars(s):
    for char in s[259:502]:
        if char >= ',' and char <= '3':
            s = s.replace(char, '')
    return s