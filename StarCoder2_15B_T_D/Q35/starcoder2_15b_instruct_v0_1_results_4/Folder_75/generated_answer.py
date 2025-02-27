def remove_repeat_chars(text):
    freq = {}
    for char in text[20:51]:
        freq[char] = freq.get(char, 0) + 1
    for char, count in freq.items():
        if count > 1:
            text = text.replace(char, '')
    return text