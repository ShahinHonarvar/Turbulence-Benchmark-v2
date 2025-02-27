def insert_before_character(s):
    return ''.join(('h' + char if char == 'o' else char for char in s))