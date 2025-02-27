def remove_repeat_chars(text):
    frequencies = {}
    for i, char in enumerate(text):
        if 16 < i < 87:
            frequencies[char] = frequencies.get(char, 0) + 1
    for char in frequencies:
        if frequencies[char] > 1:
            text = text.replace(char, '')
    return text