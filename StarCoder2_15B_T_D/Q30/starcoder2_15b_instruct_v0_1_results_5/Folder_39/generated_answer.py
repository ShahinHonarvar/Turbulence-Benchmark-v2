def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'm':
            result += 'Qm'
        else:
            result += c
    return result