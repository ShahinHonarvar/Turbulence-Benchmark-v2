def remove_repeat_chars(input_string):
    unique_chars = set()
    result = ''
    for i, char in enumerate(input_string[1:-1]):
        if char not in unique_chars:
            unique_chars.add(char)
            result += char
    return input_string[0] + result + input_string[-1]