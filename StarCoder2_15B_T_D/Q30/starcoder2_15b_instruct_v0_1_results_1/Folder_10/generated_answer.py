def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'j':
            result += 'vj'
        else:
            result += char
    return result