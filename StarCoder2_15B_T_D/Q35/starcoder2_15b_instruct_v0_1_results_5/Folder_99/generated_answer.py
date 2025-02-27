def remove_repeat_chars(text):
    chars_count = {}
    for i, char in enumerate(text):
        if i >= 450 and i < 905:
            chars_count[char] = chars_count.get(char, 0) + 1
    for char in chars_count:
        if chars_count[char] > 1:
            text = text.replace(char, '')
    return text