def insert_before_character(s):
    return ''.join(('u' + char if char == 'U' else char for char in s))