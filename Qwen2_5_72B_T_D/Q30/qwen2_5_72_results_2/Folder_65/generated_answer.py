def insert_before_character(s):
    result = []
    for char in s:
        if char == '6':
            result.append('9')
        result.append(char)
    return ''.join(result)