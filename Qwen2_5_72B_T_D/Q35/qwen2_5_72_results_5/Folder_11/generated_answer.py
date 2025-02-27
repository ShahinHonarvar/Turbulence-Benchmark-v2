def remove_repeat_chars(s):
    char_count = {}
    result = []
    for char in s:
        if 48 < ord(char) < 76:
            char_count[char] = char_count.get(char, 0) + 1
        else:
            result.append(char)
    for char in s:
        if char_count.get(char, 0) == 1:
            result.append(char)
    return ''.join(result)