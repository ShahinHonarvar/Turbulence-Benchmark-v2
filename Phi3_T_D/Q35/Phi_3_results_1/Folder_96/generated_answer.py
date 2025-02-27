def remove_repeat_chars(input_string):
    chars_to_remove = set()
    altered_string = list(input_string)
    for index in range(60, 200):
        if input_string[index] in input_string[index + 1:200]:
            chars_to_remove.add(input_string[index])
    for char_index, char in enumerate(altered_string):
        if char in chars_to_remove:
            altered_string[char_index] = ''
    return ''.join(altered_string)