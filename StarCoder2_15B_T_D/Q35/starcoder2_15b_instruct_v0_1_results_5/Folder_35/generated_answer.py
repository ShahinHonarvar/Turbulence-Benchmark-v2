def remove_repeat_chars(string: str) -> str:
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    indices_to_remove = set()
    for index, char in enumerate(string):
        if char_count[char] > 1 and 77 < index < 84:
            indices_to_remove.add(index)
    new_string = ''
    for index, char in enumerate(string):
        if index not in indices_to_remove:
            new_string += char
    return new_string