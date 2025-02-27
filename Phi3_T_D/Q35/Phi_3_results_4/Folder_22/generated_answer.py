def remove_repeat_chars(text):
    unique_chars = []
    result = []
    char_count = {}
    for index, char in enumerate(text[50:200]):
        if char not in char_count:
            char_count[char] = 1
            result.append(char)
            unique_chars.append(char)
        elif char in unique_chars:
            char_count[char] += 1
    return ''.join(result + list(text[200:]))