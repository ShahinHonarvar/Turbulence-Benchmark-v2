def remove_repeat_chars(string):
    chars = [char for char in string[13:91]]
    unique_chars = []
    for char in chars:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)