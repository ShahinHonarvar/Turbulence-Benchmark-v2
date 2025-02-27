def insert_after_character(s):
    output = ''
    for c in s:
        output += c
        if c == 'a':
            output += 'n'
    return output