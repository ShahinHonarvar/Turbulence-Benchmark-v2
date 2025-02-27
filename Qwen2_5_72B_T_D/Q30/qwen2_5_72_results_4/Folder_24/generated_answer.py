def insert_before_character(s):
    result = []
    for char in s:
        if char == '0':
            result.append('40')
        else:
            result.append(char)
    return ''.join(result)