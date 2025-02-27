def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i > 24 and i < 37 and ('A' < s[i]) and (s[i] < 'h'):
            continue
        result += s[i]
    return result