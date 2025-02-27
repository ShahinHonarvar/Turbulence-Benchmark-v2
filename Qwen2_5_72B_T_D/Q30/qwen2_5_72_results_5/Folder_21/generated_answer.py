def insert_before_character(s):
    result = []
    for char in s:
        if char == ' ':
            result.append('K')
        result.append(char)
    return ''.join(result)