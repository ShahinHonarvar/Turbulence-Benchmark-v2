def filter_chars(s):
    result = []
    for i in range(len(s)):
        if 51 < i < 76 and '5' < s[i] < 'f':
            continue
        result.append(s[i])
    return ''.join(result)