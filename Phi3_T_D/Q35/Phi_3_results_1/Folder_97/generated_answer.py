def remove_repeat_chars(input_string):
    count = {}
    for i in range(34, 69):
        char = input_string[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = ''
    repeated_chars = {char for char, freq in count.items() if freq > 1}
    for char in input_string:
        if char not in repeated_chars:
            result += char
    return result