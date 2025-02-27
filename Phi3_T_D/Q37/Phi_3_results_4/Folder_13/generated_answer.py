def filter_chars(s):
    for i in range(124, min(len(s), 854) + 1):
        if '9' <= s[i] <= 's':
            s = s.replace(s[i], '')
    return s