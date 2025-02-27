def filter_chars(s):
    result = ''
    for i in range(26, 80):
        if s[i] > '<' and s[i] < '>':
            continue
        result += s[i]
    return result