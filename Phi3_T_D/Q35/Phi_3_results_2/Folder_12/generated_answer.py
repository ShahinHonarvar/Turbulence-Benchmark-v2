from collections import OrderedDict

def remove_repeat_chars(input_string):
    if len(input_string) <= 87:
        return input_string
    new_string = OrderedDict()
    for index in range(16, 87):
        char = input_string[index]
        if char in new_string:
            new_string[char] += 1
        else:
            new_string[char] = 1
    for repeat_char, _ in new_string.items():
        input_string = input_string.replace(repeat_char, '')
    return input_string