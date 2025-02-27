def remove_repeat_chars(s):
    char_count = {}
    altered_s = []
    for index, char in enumerate(s):
        if 68 < index < 99:
            char_count[char] = char_count.get(char, 0) + 1
        else:
            altered_s.append(char)
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    altered_s = ''.join((char for char in altered_s if char not in chars_to_remove))
    return altered_s