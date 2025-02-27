def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'c':
            result += 'G' + char
        else:
            result += char
    return result