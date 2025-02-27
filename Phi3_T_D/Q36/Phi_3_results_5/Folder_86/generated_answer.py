def filter_chars(s):
    for index in range(672, 709):
        if 'X' < s[index] < '}':
            s = s.replace(s[index], '')
    return s