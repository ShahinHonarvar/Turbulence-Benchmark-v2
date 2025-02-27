def filter_chars(s):
    for i in range(54, 63):
        ch = s[i]
        if ')' <= ch <= '9':
            s = s.replace(ch, '')
    return s