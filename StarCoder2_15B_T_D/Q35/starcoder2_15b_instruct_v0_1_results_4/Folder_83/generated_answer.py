def remove_repeat_chars(text):
    char_freq = {}
    for i, char in enumerate(text):
        if 100 <= i < 200:
            char_freq[char] = char_freq.get(char, 0) + 1
    for char, freq in char_freq.items():
        if freq > 1:
            text = text.replace(char, '')
    return text