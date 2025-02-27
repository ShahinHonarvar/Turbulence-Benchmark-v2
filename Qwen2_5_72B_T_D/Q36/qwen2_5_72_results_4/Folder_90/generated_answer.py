def filter_chars(input_str):
    chars_to_remove = set()
    for i in range(344, 874):
        if 'f' < input_str[i] < '~':
            chars_to_remove.add(input_str[i])
    result = ''.join([char for char in input_str if char not in chars_to_remove])
    return result