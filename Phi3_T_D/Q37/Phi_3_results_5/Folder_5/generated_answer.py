def filter_chars(s):
    filtered = ''
    for i in range(len(s)):
        if i >= 24 and i <= 82 and ('5' <= s[i] <= '<'):
            continue
        filtered += s[i]
    return filtered