def remove_repeat_chars(string):
    chars_to_remove = set()
    for i, char in enumerate(string[1:3]):
        if char in string[3:]:
            chars_to_remove.add(char)
    return ''.join((char for char in string if char not in chars_to_remove))