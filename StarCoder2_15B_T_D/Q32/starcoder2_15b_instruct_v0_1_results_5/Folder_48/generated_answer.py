def insert_after_character(s):
    output = ''
    for c in s:
        if c == 'S':
            output += 'SU'
        else:
            output += c
    return output