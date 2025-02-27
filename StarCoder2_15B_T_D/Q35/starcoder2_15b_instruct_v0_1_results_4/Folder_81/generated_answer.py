def remove_repeat_chars(my_string: str) -> str:
    char_counts = {}
    for char in my_string[20:200]:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    new_string = ''
    for char in my_string:
        if char not in repeated_chars:
            new_string += char
    return new_string