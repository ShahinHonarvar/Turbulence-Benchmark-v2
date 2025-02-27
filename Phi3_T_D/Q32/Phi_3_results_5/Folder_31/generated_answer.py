def insert_after_character(source):
    modified_string = ''.join(['BN' if char == 'B' else char for char in source])
    return modified_string