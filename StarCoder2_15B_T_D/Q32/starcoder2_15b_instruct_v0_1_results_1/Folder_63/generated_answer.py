def insert_after_character(s):
    output = ''
    for c in s:
        output += c
        if c == '5':
            output += 'R'
    return output