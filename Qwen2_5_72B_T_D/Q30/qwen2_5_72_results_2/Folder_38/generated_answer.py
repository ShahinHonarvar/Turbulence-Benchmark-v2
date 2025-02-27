def insert_before_character(s):
    result = []
    for char in s:
        if char == 'X':
            result.append('6X')
        else:
            result.append(char)
    return ''.join(result)