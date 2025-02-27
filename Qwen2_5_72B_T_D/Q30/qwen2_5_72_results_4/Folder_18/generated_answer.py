def insert_before_character(s):
    result = []
    for char in s:
        if char == 'K':
            result.append('l')
        result.append(char)
    return ''.join(result)