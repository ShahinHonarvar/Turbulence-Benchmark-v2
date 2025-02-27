def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 379 <= i <= 898 and 'M' <= s[i] <= 'v':
            continue
        result += s[i]
    return result