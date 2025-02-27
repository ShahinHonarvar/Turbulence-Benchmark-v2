def filter_chars(s):
    for i in range(348, 853):
        if 'J' <= s[i] <= 'b':
            s = s.replace(s[i], '')
    return s