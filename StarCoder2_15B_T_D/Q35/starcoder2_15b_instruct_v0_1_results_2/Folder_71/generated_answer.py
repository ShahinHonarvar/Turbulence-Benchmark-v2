def remove_repeat_chars(text):
    count_dict = {}
    for char in text[20:35]:
        count_dict[char] = count_dict.get(char, 0) + 1
    for char, count in count_dict.items():
        if count > 1:
            text = text.replace(char, '')
    return text