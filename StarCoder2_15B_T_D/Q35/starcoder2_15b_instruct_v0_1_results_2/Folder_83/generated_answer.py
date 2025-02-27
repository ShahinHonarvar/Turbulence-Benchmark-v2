def remove_repeat_chars(text):
    count_chars = {}
    for i, char in enumerate(text):
        if i < 100 or i >= 200:
            continue
        count_chars[char] = count_chars.get(char, 0) + 1
    for char, count in count_chars.items():
        if count > 1:
            text = text.replace(char, '')
    return text