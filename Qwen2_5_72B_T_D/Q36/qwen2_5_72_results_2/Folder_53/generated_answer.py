def filter_chars(s):
    result = []
    for i in range(len(s)):
        if 90 < i < 97 and 'j' < s[i] < 'w':
            continue
        result.append(s[i])
    return ''.join(result)