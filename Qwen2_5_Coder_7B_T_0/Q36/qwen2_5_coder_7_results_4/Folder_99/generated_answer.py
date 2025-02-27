def filter_chars(s):
    target_chars = set('cd')
    result = []
    for i, char in enumerate(s):
        if not 476 < i < 948 or char not in target_chars:
            result.append(char)
    return ''.join(result)