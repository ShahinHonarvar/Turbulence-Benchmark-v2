def insert_before_character(s):
    return ''.join(('O' + char if char == 'o' else char for char in s))