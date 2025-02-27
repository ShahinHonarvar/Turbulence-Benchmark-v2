def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'I':
            result += 'i' + char
        else:
            result += char
    return result