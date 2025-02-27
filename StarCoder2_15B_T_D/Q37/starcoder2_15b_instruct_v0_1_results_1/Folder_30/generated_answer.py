def filter_chars(s):
    for i in range(len(s)):
        if 41 <= i <= 64 and 'K' <= s[i] <= ']':
            s = s.replace(s[i], '')
    return s