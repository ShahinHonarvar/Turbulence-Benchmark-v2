def filter_chars(s):
    target_chars = set('012345678')
    result = []
    for i, char in enumerate(s):
        if not (384 <= i <= 411 and char in target_chars):
            result.append(char)
    return ''.join(result)