def filter_chars(s):
    filtered = ''
    for i in range(12, 78):
        if ':' <= s[i] <= 'L':
            continue
        filtered += s[i]
    return filtered