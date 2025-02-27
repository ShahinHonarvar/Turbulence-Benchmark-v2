def insert_before_character(s):
    return ''.join(('o' + char if char == 'O' else char for char in s))