def insert_before_character(s):
    result = ''
    for char in s:
        result += 'a' if char == 'U' else char
    return result