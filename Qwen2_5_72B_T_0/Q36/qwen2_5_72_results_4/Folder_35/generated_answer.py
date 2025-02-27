def filter_chars(s):
    for i in range(163, 658):
        char = s[i]
        if '(' < char < ']':
            s = s.replace(char, '')
    return s