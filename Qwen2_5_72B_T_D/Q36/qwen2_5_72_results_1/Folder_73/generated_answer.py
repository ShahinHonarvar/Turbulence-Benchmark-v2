def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if not (66 < i < 90 and '#' < s[i] < 'T'):
            result += s[i]
    return result