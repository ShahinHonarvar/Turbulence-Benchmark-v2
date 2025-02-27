def filter_chars(input_string):
    target_range = input_string[19:33]
    characters_to_remove = [char for char in target_range if 'f' <= char <= 'o']
    for char in characters_to_remove:
        input_string = input_string.replace(char, '')
    return input_string