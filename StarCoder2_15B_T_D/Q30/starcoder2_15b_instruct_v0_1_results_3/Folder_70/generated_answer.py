def insert_before_character(string):
    result = []
    for character in string:
        result.append(character)
        if character == 'P':
            result.append('V')
    return ''.join(result)