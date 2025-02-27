def insert_before_character(s):
    result = []
    for char in s:
        if char == 'P':
            result.append('V')
        result.append(char)
    return ''.join(result)