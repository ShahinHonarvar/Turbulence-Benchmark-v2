def remove_repeat_chars(string):
    chars = {}
    for i, char in enumerate(string):
        if i >= 49 and i < 74:
            if char not in chars:
                chars[char] = []
            chars[char].append(i)
    for char in chars:
        if len(chars[char]) > 1:
            string = string.replace(char, '')
    return string