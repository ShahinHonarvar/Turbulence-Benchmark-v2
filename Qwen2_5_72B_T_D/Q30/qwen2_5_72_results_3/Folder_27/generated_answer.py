def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'N':
            result += 'j' + char
        else:
            result += char
    return result