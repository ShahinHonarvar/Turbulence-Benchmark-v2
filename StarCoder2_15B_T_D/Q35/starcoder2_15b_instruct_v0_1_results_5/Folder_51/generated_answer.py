def remove_repeat_chars(text):
    count = {}
    for char in text:
        count[char] = count.get(char, 0) + 1
    result = []
    for char in text:
        if count[char] == 1 or (text.index(char) < 6 or text.index(char) >= 9):
            result.append(char)
    return ''.join(result)