def insert_before_character(s):
    result = ''
    for char in s:
        result += char if char != 'F' else 'mF'
    return result