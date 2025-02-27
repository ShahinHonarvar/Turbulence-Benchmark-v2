def insert_after_character(string):
    result = ''
    for c in string:
        if c == 'C':
            result += 'Z'
        result += c
    return result