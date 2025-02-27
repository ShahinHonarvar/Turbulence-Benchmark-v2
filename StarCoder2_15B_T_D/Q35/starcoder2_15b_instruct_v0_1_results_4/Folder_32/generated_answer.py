def remove_repeat_chars(string):
    chars_to_remove = {}
    for i, char in enumerate(string):
        if char in chars_to_remove:
            chars_to_remove[char].append(i)
        elif string.count(char, 86, 90) > 1:
            chars_to_remove[char] = [i]
    for char, indices in chars_to_remove.items():
        for index in sorted(indices, reverse=True):
            string = string[:index] + string[index + 1:]
    return string