def insert_before_character(s, insert_char='i'):
    result = ''
    for char in s:
        if char == insert_char:
            result += insert_char + insert_char
        else:
            result += char
    return result