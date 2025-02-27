def remove_repeat_chars(input_string):
    chars_to_remove = set()
    for i in range(52, 75):
        if input_string[i] in input_string[52:75]:
            chars_to_remove.add(input_string[i])
    result = []
    for char in input_string:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)