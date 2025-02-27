def insert_before_character(s):
    return ''.join((f'y{char}' if char == 'b' else char for char in s))