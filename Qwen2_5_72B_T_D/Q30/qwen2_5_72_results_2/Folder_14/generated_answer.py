def insert_before_character(s):
    return ' '.join([' ' + char if char == ' ' and idx > 0 else char for idx, char in enumerate(s)])