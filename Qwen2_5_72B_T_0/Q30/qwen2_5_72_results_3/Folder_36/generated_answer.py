def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'A':
            result += 'H' + char
        else:
            result += char
    return result