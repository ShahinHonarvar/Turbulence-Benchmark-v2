def remove_repeat_chars(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in char_count:
        if char_count[char] > 1 and 50 < text.index(char) < 92:
            text = text.replace(char, '')
    return text