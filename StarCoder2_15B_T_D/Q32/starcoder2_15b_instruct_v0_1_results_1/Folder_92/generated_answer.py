def insert_after_character(string):
    output = ''
    for i, c in enumerate(string):
        output += c
        if c == 'a':
            output += 'a'
    return output