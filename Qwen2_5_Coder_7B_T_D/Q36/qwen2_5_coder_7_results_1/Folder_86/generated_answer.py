def filter_chars(s):
    for i in range(672, 709):
        char = chr(i)
        if 'X' < char < '}':
            s = s.replace(char, '')
    return s