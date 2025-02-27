def remove_repeat_chars(input_string):
    char_freq = {}
    for i in range(35, 63):
        char = input_string[i]
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    to_remove = [char for char, freq in char_freq.items() if freq > 1]
    result = [char for char in input_string if char not in to_remove]
    return ''.join(result)