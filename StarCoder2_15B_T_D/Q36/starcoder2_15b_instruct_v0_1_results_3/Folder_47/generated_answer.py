def filter_chars(string):
    result = []
    for i, c in enumerate(string):
        if i >= 45 and i < 57 and (ord(c) > ord('F')) and (ord(c) < ord('n')):
            continue
        result.append(c)
    return ''.join(result)