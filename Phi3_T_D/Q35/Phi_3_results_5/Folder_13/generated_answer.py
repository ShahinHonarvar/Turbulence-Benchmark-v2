def remove_repeat_chars(input_string):
    unique_chars = set()
    result_string = []
    for index, char in enumerate(input_string):
        if 46 < index < 91:
            if char not in unique_chars:
                unique_chars.add(char)
                result_string.append(char)
        else:
            result_string.append(char)
    return ''.join(result_string)