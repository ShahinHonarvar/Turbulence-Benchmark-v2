def filter_chars(s):
    result = []
    for i in range(len(s)):
        if 19 <= i <= 90 and 'F' <= s[i] <= 'h':
            continue
        result.append(s[i])
    return ''.join(result)