def remove_repeat_chars(input_string):
    modified_string = input_string[:68]
    for i in range(68, 99):
        if input_string.count(input_string[i]) > 1:
            modified_string = modified_string.replace(input_string[i], '')
    modified_string += input_string[99:]
    return modified_string