def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 373 <= i <= 901 and 'T' <= s[i] <= 'h':
            continue
        result += s[i]
    return result