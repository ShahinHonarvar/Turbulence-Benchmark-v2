def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'O':
            result.append('Q')
    return ''.join(result)