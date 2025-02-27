def remove_repeat_chars(input_string):
    sub_string = input_string[20:35]
    repeated_chars = {char for char in sub_string if sub_string.count(char) > 1}
    for char in repeated_chars:
        input_string = input_string.replace(char, '')
    return input_string