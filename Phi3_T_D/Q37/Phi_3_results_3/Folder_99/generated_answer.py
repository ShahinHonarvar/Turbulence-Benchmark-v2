def filter_chars(s):
    result = []
    for i in range(373, 902):
        if 373 <= i <= 901 and 'T' <= s[i] <= 'h':
            continue
        result.append(s[i])
    return ''.join(result)