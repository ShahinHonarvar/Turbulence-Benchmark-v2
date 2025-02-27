def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'A':
            result += 'aA'
        else:
            result += char
    return result