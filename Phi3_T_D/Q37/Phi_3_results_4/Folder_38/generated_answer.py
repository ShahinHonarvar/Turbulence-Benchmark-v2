def filter_chars(s):
    seq = range(24, 80)
    result = ''
    for i in range(len(s)):
        if i in seq and 'a' <= s[i] <= 'f':
            continue
        result += s[i]
    return result