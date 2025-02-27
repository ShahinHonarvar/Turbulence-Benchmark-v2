def remove_repeat_chars(text):
    start, end = (45, 48)
    substr = set(text[start:end])
    for char in substr:
        if text.count(char, start, end) > 1:
            text = text.replace(char, '', 1)
    return text