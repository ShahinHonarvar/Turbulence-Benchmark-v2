def remove_repeat_chars(text):
    count = {}
    for char in text[10:100]:
        count[char] = count.get(char, 0) + 1
    for char, freq in count.items():
        if freq > 1:
            text = text.replace(char, '')
    return text