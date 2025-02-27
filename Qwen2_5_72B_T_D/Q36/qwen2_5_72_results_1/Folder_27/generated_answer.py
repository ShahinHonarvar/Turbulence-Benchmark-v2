def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if not (48 < i < 75 and '6' < s[i] < '_'):
            result += s[i]
    return result