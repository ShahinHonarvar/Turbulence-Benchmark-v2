from collections import OrderedDict

def remove_repeat_chars(input_string):
    char_count = OrderedDict()
    new_string = ''
    for i, char in enumerate(input_string[29:53]):
        if char in char_count:
            char_count[char][1] += 1
        else:
            char_count[char] = [i + 29, 1]
    for i in range(len(input_string)):
        if i + 29 < len(char_count) and char_count[input_string[i]] < char_count[input_string[i]][1]:
            continue
        new_string += input_string[i]
    return new_string