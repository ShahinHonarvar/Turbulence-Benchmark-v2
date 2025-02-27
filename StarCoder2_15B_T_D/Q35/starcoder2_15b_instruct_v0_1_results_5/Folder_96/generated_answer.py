def remove_repeat_chars(text: str) -> str:
    char_count = {}
    for char in text[60:200]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = [char for char, count in char_count.items() if count > 1]
    new_text = ''
    for char in text:
        if char not in chars_to_remove:
            new_text += char
    return new_text