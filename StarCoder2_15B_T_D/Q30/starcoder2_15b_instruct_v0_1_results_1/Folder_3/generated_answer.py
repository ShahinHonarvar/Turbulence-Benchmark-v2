def insert_before_character(s):
    result = ''
    for c in s:
        if c == '0':
            result += 'H0'
        else:
            result += c
    return result