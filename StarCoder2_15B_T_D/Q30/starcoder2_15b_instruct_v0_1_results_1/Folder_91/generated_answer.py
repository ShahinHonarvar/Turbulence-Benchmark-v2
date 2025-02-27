def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'a':
            result += string[i - 1:i] + '0'
        result += c
    return result