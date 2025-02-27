def remove_repeat_chars(s):
    chars_count = {}
    result_chars = []
    for index, char in enumerate(s):
        if 10 < index < 79:
            chars_count[char] = chars_count.get(char, 0) + 1
        if chars_count.get(char, 0) == 1:
            result_chars.append(char)
        if index > 79 and all((count <= 1 for count in chars_count.values())):
            break
    return ''.join(result_chars)