def insert_after_character(s):
    return ''.join(('n' + char if char == 'H' else char for char in s))