def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'u':
            result += 'u' * 2
        else:
            result += char
    return result