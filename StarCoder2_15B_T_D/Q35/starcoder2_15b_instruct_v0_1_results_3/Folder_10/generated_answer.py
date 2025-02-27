def remove_repeat_chars(text):
    for i in range(36, 54):
        count = text.count(text[i])
        if count > 1:
            text = text.replace(text[i], '')
    return text