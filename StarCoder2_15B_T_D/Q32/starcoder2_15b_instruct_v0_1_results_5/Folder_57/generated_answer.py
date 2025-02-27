def insert_after_character(s):
    output = ''
    for i, c in enumerate(s):
        output += c
        if c == 's':
            output += 'w'
    return output