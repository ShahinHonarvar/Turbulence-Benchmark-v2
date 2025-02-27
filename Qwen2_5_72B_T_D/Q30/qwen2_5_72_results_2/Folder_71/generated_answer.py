def insert_before_character(s):
    result = []
    for char in s:
        if char == '2':
            result.append('S')
        result.append(char)
    return ''.join(result)