def insert_after_character(s):
    result = []
    for c in s:
        result.append(c)
        if c == 'B':
            result.append('N')
    return ''.join(result)