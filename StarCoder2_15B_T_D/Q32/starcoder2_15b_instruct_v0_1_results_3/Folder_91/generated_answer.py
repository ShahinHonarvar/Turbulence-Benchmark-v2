def insert_after_character(s):
    result = []
    for c in s:
        result.append(c)
        if c == 'a':
            result.append('0')
    return ''.join(result)