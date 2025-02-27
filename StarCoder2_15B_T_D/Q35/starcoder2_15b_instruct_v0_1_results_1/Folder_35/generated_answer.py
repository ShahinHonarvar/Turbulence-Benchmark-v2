def remove_repeat_chars(text):
    for i, c in enumerate(text):
        if text.count(c) > 1 and 77 < i < 84:
            text = ''.join([ch for ch in text if ch != c])
    return text