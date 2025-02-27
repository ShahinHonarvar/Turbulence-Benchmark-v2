def insert_before_character(s):
    result = []
    for char in s:
        if char == 'x':
            result.append('N')
        result.append(char)
    return ''.join(result)