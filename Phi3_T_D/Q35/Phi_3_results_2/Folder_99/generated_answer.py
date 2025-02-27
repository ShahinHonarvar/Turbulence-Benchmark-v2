def remove_repeat_chars(input_string):
    sub_string = input_string[450:905]
    seen = set()
    result = ''
    for char in input_string:
        if 450 <= input_string.index(char) < 905 and char in seen:
            continue
        else:
            seen.add(char)
            result += char
    return result