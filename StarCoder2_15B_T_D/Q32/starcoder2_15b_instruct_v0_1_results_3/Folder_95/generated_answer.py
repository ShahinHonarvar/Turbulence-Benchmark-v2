def insert_after_character(s):
    output = ''
    for c in s:
        output += c
        if c == 'j':
            output += 'q'
    return output