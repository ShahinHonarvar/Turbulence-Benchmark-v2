def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if not (32 < i < 61 and '3' < s[i] < 'D'):
            result += s[i]
    return result