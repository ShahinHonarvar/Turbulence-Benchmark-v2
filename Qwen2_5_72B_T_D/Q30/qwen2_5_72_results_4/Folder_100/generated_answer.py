def insert_before_character(s):
    result = []
    for char in s:
        if char == '0':
            result.append(' ')
        result.append(char)
    return ''.join(result)