def remove_repeat_chars(text):
    for char in set(text[200:202]):
        if text.count(char) > 1:
            text = text.replace(char, '')
    return text