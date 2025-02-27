def remove_repeat_chars(text):
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    result = []
    for char in text:
        if char_freq[char] > 1:
            continue
        result.append(char)
    return ''.join(result)