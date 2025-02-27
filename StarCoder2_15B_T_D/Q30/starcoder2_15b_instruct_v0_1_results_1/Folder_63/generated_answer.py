def insert_before_character(s):
    result = []
    for c in s:
        if c == '5':
            result.append('R')
        result.append(c)
    return ''.join(result)