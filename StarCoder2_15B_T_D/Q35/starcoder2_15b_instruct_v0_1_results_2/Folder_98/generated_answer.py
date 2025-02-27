def remove_repeat_chars(text):
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    for char, freq in char_freq.items():
        if freq > 1:
            text = text.replace(char, '')
    return text