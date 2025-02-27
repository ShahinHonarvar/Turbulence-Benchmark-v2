def filter_chars(s):
    result = []
    for i in range(len(s)):
        if 12 <= i <= 88 and '&' <= s[i] <= 'v':
            continue
        result.append(s[i])
    return ''.join(result)