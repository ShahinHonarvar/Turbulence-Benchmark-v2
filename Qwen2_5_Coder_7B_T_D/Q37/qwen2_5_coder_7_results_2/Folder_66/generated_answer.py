def filter_chars(s):
    target_chars = set('cdefghi')
    result = ''
    for i, char in enumerate(s):
        if i >= 27 and i <= 85 and (char in target_chars):
            continue
        result += char
    return result