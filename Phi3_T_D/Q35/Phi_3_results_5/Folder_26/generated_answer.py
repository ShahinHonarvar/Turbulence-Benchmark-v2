def remove_repeat_chars(input_string):
    char_count = {}
    i = 0
    while i < len(input_string):
        if i >= 68 and i < 99:
            char = input_string[i]
            char_count[char] = char_count.get(char, 0) + 1
        i += 1
    result = []
    for char in input_string:
        if char not in char_count or char_count[char] == 1:
            result.append(char)
    return ''.join(result)