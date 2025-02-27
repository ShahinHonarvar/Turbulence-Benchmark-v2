def remove_repeat_chars(input_string):
    indices = range(39, 44)
    char_to_remove = set((input_string[i] for i in indices))
    result = [char for char in input_string if char not in char_to_remove or char_to_remove.count(char) <= 1]
    return ''.join(result)