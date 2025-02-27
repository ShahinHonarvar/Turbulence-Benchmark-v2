def insert_after_character(input_str):
    result = []
    for character in input_str:
        result.append(character)
        if character == 'g':
            result.append('t')
    return ''.join(result)