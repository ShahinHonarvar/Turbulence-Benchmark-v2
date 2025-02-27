def filter_chars(s):
    for i in range(299, 418):
        if '9' < s[i] < 'P':
            s = s.replace(s[i], '')
    return s