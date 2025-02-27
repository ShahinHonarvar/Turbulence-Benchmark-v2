def insert_after_character(s):
    result = ''
    for i, c in enumerate(s):
        if c == 'R':
            result += 'RV'
        else:
            result += c
    return result