def insert_before_character(string):
    result = []
    for char in string:
        if char == 'Q':
            result.append('I')
        result.append(char)
    return ''.join(result)