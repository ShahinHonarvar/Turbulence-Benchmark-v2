def filter_chars(s):
    res = []
    for i in range(len(s)):
        if 72 <= i <= 94 and '.' <= s[i] <= 'b':
            continue
        res.append(s[i])
    return ''.join(res)