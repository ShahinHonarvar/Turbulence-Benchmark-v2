def remove_repeat_chars(s):
    char_count = {}
    for i in range(33, 100):
        char_count[chr(i)] = 0
    for char in s:
        if 33 <= ord(char) <= 99:
            char_count[char] += 1
    result = ''
    for char in s:
        if char_count[char] == 1 or not 33 <= ord(char) <= 99:
            result += char
    return result