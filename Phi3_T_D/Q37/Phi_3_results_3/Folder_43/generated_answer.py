def filter_chars(s):
    altered = ''
    for i in range(len(s)):
        if 15 <= i <= 55 and 'W' <= s[i] <= '{':
            continue
        altered += s[i]
    return altered