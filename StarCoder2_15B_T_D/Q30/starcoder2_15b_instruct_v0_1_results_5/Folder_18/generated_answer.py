def insert_before_character(s):
    output = ''
    for c in s:
        if c == 'K':
            output += 'lK'
        else:
            output += c
    return output