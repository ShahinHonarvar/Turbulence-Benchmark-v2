def remove_repeat_chars(string):
    chars = list(string)
    for i, c in enumerate(chars):
        if chars.count(c) > 1 and i >= 0 and (i < 5):
            chars = [x for x in chars if x != c]
    return ''.join(chars)