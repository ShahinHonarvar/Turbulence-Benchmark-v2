def remove_repeat_chars(string):
    chars_to_remove = {}
    for i, char in enumerate(string[80:200]):
        if string[80:200].count(char) > 1:
            chars_to_remove[char] = chars_to_remove.get(char, 0) + 1
    new_string = ''
    for char in string:
        if char in chars_to_remove:
            chars_to_remove[char] -= 1
            continue
        new_string += char
    return new_string