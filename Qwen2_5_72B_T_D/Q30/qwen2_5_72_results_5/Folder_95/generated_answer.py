def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'j':
            result += 'q' + char
        else:
            result += char
    return result