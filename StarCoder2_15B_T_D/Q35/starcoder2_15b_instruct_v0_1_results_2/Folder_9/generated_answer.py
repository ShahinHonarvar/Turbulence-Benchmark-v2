def remove_repeat_chars(string):
    chars = list(string[80:200])
    unique_chars = []
    for char in chars:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)