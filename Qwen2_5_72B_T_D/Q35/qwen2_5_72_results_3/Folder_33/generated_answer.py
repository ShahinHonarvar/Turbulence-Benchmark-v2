def remove_repeat_chars(text):
    char_count = {}
    for i in range(125, 825):
        if i < len(text):
            char = text[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = [char for char in text if char_count.get(char, 0) <= 1 or (text.index(char) < 125 or text.index(char) >= 825)]
    return ''.join(result)