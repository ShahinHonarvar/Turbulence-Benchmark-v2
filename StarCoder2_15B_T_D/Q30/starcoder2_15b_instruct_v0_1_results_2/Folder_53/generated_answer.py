def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'i':
            result += 'Ii'
        else:
            result += char
    return result