def filter_chars(s):
    for i in range(82, 89):
        char = s[i]
        if '*' < char < '[':
            s = s.replace(char, '')
    return s