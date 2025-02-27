def remove_repeat_chars(input_string):
    char_count = {}
    for i in range(25, 80):
        if input_string[i] in char_count:
            char_count[input_string[i]] += 1
        else:
            char_count[input_string[i]] = 1
    result = ''
    for char in input_string:
        if char_count[char] <= 1:
            result += char
    return result