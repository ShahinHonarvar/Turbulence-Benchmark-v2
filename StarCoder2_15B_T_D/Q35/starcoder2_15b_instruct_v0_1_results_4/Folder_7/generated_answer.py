def remove_repeat_chars(string: str) -> str:
    char_indices = dict()
    result = ''
    for i, char in enumerate(string):
        if char in char_indices:
            if 375 < char_indices[char] < 926:
                continue
        char_indices[char] = i
        result += char
    return result