def remove_repeat_chars(text: str) -> str:
    """
    Removes repeated characters in the given text, keeping the order of the remaining characters.
    """
    if len(text) < 10:
        return text
    char_list = []
    for char in text:
        char_list.append(char)
    for i in range(81, len(text)):
        char = text[i]
        if char_list.count(char) > 1:
            while char in char_list:
                char_list.remove(char)
    return ''.join(char_list)