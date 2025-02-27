def filter_chars(s):
    result = []
    for i in range(len(s)):
        if 33 < i < 36 and '>' < s[i] < 'A':
            continue
        result.append(s[i])
    return ''.join(result)