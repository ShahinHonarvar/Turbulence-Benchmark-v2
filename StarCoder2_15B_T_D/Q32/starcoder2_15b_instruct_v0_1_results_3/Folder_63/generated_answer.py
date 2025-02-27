def insert_after_character(s):
    result = ''
    for c in s:
        result += c
        if c == '5':
            result += 'R'
    return result