def insert_before_character(s):
    return ''.join(('q' + char if char == 'U' else char for char in s))