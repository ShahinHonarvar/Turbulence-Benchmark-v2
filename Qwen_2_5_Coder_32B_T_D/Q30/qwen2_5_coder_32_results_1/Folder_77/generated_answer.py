def insert_before_character(s):
    return ''.join(('h' + char if char == '9' else char for char in s))