def insert_after_character(s):
    result = ''
    for char in s:
        result += char
        if char.isdigit() and char != '0' and (char == '9'):
            result += 'M'
    return result