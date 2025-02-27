def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'N':
            result += 'Nj'
        else:
            result += char
    return result