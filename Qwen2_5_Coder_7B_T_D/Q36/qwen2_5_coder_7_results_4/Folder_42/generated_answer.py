def filter_chars(s):
    char_set = set('tuvwx')
    result = []
    for i, char in enumerate(s):
        if 42 < i < 68 and char in char_set:
            continue
        result.append(char)
    return ''.join(result)