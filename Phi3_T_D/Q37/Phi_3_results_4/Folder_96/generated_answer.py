def filter_chars(input_string):
    if not 86 <= len(input_string) <= 92:
        return input_string
    chars_to_remove = []
    for i in range(86, 93):
        if '!' <= input_string[i] <= 's':
            chars_to_remove.append(input_string[i])
    filtered_string = input_string
    for char in chars_to_remove:
        filtered_string = filtered_string.replace(char, '')
    return filtered_string