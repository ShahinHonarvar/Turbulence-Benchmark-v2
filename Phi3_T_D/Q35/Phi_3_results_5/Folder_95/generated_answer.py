def remove_repeat_chars(input_string):
    modified_chars = []
    char_frequency = {}
    for char in input_string:
        index = ord(char)
        if 32 < index < 99:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
            if char_frequency[char] == 1:
                modified_chars.append(char)
    return ''.join(modified_chars)