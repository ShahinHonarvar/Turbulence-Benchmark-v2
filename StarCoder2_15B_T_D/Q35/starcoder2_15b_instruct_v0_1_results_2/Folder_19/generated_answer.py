def remove_repeat_chars(text):
    for char in text[1:4]:
        if text.count(char) > 1:
            text = text.replace(char, '')
    return text