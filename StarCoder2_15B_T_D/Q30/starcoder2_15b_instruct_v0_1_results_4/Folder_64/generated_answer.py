def insert_before_character(string):
    output = ''
    for i, c in enumerate(string):
        if c == 'u':
            output += 'u'
        output += c
    return output