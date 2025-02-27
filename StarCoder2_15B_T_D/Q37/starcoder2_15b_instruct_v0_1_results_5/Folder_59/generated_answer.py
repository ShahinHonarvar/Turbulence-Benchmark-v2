def filter_chars(s):
    for i in range(len(s)):
        if i >= 2 and i <= 3 and (ord(s[i]) >= ord('5')) and (ord(s[i]) <= ord('_')):
            s = s.replace(s[i], '')
    return s