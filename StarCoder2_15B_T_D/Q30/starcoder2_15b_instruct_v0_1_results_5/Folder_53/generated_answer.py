def insert_before_character(string):
    return ''.join([f'I{c}' if c == 'i' else c for c in string])