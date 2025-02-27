def remove_repeat_chars(text):
    count = {}
    for char in text[80:200]:
        count[char] = count.get(char, 0) + 1
    for char in set(text[80:200]):
        if count[char] > 1:
            text = text.replace(char, '')
    return text