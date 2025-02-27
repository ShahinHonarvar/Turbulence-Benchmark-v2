def insert_before_character(s):
    result = ''
    for char in s:
        result += 'j' if char == 'O' else char
    return result