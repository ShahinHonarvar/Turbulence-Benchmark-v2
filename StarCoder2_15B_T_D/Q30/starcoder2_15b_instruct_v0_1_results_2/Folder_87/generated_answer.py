def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'm':
            result += 'N'
        result += c
    return result