def insert_after_character(s):
    result = ''
    for char in s:
        result += char
        if char == 'T':
            result += ' '
    return result.strip()