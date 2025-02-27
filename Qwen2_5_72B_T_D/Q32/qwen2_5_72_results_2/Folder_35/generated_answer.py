def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == '9':
            result.append('M')
    return ''.join(result)