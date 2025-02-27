def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'I':
            result += 'II'
        else:
            result += char
    return result