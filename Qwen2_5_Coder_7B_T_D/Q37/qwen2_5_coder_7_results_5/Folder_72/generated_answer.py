def filter_chars(s):
    chars_to_remove = set('HJKLMNPQRStuv')
    result = []
    for i in range(len(s)):
        if i < 35 or i > 51 or s[i] not in chars_to_remove:
            result.append(s[i])
    return ''.join(result)