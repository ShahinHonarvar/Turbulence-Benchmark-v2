def remove_repeat_chars(input_string):
    unique_chars = []
    modified_chars = []
    for i, char in enumerate(input_string):
        if 476 < i < 709 and char not in unique_chars:
            unique_chars.append(char)
            modified_chars.append(char)
        elif 476 < i < 709 and char in unique_chars:
            continue
        else:
            modified_chars.append(char)
    return ''.join(modified_chars)