def filter_chars(s):
    result = ''
    for idx in range(12, 89):
        char = s[idx]
        if '&' <= char <= 'v':
            continue
        result += char
    return result[12:] + result[:12] + result[89:]