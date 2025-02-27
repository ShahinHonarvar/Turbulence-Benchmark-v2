def filter_chars(s):
    for i in range(323, 526):
        if ')' < s[i] < 'O':
            s = s.replace(s[i], '')
    return s