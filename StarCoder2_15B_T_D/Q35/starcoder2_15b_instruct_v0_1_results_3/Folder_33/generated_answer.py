def remove_repeat_chars(text):
    char_count = {}
    for char in text[125:825]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            text = text.replace(char, '')
    return text