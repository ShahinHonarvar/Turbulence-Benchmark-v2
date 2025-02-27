def insert_before_character(s):
    return ''.join(('I' + char if char == 'i' else char for char in s))