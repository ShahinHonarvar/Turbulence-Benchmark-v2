def insert_before_character(s):
    result = ''
    for char in s:
        if char == ' ':
            result += 'W'
        result += char
    return result