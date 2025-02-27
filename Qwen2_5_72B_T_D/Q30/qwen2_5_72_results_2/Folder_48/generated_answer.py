def insert_before_character(s):
    result = []
    for char in s:
        if char == 'S':
            result.append('U')
        result.append(char)
    return ''.join(result)