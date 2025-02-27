def remove_repeat_chars(text):
    char_count = {}
    for i in range(13, 91):
        if i < len(text):
            char = text[i]
            char_count[char] = char_count.get(char, 0) + 1
    result = [char for char in text if char_count.get(char, 0) <= 1 or (len(result) < 13 or len(result) >= 91)]
    return ''.join(result)