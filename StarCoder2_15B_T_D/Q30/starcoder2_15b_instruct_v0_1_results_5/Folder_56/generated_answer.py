def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'I':
            result += 'iI'
        else:
            result += c
    return result