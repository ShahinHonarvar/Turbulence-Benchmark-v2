def filter_chars(s):
    for i in range(672, 709):
        char = s[i]
        if 'X' < char < '}':
            s = s.replace(char, '')
    return s