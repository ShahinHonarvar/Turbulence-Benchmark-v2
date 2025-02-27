def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 19 <= i <= 92 and '8' <= s[i] <= 'm':
            continue
        result += s[i]
    return result