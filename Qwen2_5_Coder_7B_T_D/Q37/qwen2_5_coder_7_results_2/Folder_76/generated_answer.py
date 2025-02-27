def filter_chars(s):
    target_chars = set('MmNnOoPpQqRrSsTtUuVv')
    result = []
    for i, char in enumerate(s):
        if not 379 <= i <= 898 or char not in target_chars:
            result.append(char)
    return ''.join(result)