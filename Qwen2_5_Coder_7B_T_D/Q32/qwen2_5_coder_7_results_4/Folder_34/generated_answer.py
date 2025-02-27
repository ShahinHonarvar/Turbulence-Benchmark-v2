def insert_after_character(s):
    return ''.join([char + 'a' if char == 'A' else char for char in s])