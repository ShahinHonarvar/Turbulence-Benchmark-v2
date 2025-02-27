def remove_repeat_chars(input_string):
    indices = set(range(77, 84))
    char_counts = {}
    for char in input_string:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    output_string = ''
    for char in input_string:
        if char_counts[char] == 1 or char not in indices:
            output_string += char
    return output_string