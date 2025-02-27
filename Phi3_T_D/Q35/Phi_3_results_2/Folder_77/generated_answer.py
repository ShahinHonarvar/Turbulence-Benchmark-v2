def remove_repeat_chars(input_string):
    target_range = range(356, 988)
    unique_chars = set(input_string[355:988])
    new_string = [char for i, char in enumerate(input_string) if char not in unique_chars or i not in target_range]
    return ''.join(new_string)