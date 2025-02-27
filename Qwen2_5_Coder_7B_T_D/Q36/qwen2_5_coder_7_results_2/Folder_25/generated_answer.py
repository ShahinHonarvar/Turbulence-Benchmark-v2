def filter_chars(input_string):
    chars_to_remove = set()
    for i in range(24, 37):
        if 'A' < input_string[i] < 'h':
            chars_to_remove.add(input_string[i])
    result = []
    for char in input_string:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)