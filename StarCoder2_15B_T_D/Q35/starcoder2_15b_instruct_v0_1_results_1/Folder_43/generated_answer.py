def remove_repeat_chars(string):
    char_counts = {}
    for i, char in enumerate(string):
        if i < 10 or i >= 28:
            continue
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    chars_to_remove = [char for char, count in char_counts.items() if count > 1]
    new_string = ''
    for char in string:
        if char not in chars_to_remove:
            new_string += char
    return new_string