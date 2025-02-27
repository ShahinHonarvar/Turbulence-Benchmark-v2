def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'A':
            result += 'HA'
        else:
            result += char
    return result