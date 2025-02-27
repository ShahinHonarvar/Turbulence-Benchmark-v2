def insert_before_character(string):
    result = ''
    for i, char in enumerate(string):
        if char == 'c':
            result += 'G'
        result += char
    return result