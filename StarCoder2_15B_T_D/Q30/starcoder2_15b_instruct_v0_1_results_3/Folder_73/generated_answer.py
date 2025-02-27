def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'R':
            result += 'VR'
        else:
            result += char
    return result