def remove_repeat_chars(input_str):
    unique_chars = []
    for i in range(44, 78):
        char = input_str[i]
        if char not in unique_chars:
            unique_chars.append(char)
    altered_str = ''.join(unique_chars)
    return altered_str