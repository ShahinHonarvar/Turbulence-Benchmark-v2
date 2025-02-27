def remove_repeat_chars(string):
    char_count = {}
    for char in string[13:76]:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    output = []
    for char in string:
        if char not in repeated_chars:
            output.append(char)
    return ''.join(output)