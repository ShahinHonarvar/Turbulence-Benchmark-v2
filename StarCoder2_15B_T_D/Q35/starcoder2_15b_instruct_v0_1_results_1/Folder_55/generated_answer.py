def remove_repeat_chars(string):
    chars_count = {}
    for char in string:
        chars_count[char] = chars_count.get(char, 0) + 1
    indexes_to_remove = []
    for i, char in enumerate(string):
        if chars_count[char] > 1 and 10 < i < 100:
            indexes_to_remove.append(i)
    new_string = ''
    for i, char in enumerate(string):
        if i not in indexes_to_remove:
            new_string += char
    return new_string