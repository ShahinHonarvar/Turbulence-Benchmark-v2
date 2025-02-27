def remove_repeat_chars(text):
    chars_to_remove = set()
    for i in range(81, 86):
        if text.count(text[i]) > 1:
            chars_to_remove.add(text[i])
    filtered_text = ''.join((c for c in text if c not in chars_to_remove))
    return filtered_text