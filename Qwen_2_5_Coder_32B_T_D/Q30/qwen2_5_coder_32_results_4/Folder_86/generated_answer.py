def insert_before_character(s):
    return ''.join(('Q' + char if char == 'O' else char for char in s))