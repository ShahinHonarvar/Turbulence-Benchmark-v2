def filter_chars(s):
    target_chars = set('EFGH')
    result = []
    for i, char in enumerate(s):
        if i not in range(421, 854) or char not in target_chars:
            result.append(char)
    return ''.join(result)