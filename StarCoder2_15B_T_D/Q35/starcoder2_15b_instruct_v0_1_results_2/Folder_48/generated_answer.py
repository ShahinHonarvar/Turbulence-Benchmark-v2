def remove_repeat_chars(string):
    substring = string[409:502]
    char_freq = {}
    for char in substring:
        char_freq[char] = char_freq.get(char, 0) + 1
    unique_chars = [char for char in char_freq if char_freq[char] > 1]
    new_string = ''
    for char in string:
        if char not in unique_chars:
            new_string += char
    return new_string