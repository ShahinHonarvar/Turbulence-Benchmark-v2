def insert_after_character(s):
    result = []
    for c in s:
        result.append(c)
        if c == 'u':
            result.append('U')
    return ''.join(result)