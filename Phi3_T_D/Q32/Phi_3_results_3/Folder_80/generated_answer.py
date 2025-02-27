def insert_after_character(input_string, char_to_insert='X', target_char=' '):
    return input_string.replace(target_char, f'{target_char}{char_to_insert}')