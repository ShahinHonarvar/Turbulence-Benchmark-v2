def insert_after_character(string):
    result = []
    for char in string:
        result.append(char)
        if char == 'X':
            result.append('6')
    return ''.join(result)