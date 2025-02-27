def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'o':
            result += 'h'
        result += char
    return result