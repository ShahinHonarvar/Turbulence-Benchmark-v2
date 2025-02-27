def filter_chars(s):
    to_remove = set('BCDEFGHIJKLMNPQRSTUVWXYZ')
    result = []
    for i, char in enumerate(s):
        if i in range(154, 222) and char in to_remove:
            continue
        result.append(char)
    return ''.join(result)