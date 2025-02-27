def remove_repeat_chars(s):
    char_count = {}
    result = ''
    for char in s:
        if 32 < ord(char) < 99:
            char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char not in char_count or char_count[char] == 1:
            result += char
    return result