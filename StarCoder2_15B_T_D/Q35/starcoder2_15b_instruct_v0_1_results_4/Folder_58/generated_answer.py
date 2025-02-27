def remove_repeat_chars(text):
    return ''.join(sorted(set(text), key=text.index))