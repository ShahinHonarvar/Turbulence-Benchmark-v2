def remove_repeat_chars(s):
    char_count = {}
    for char in s:
        if 32 < ord(char) < 99:
            char_count[char] = char_count.get(char, 0) + 1
    result = ''.join([char for char in s if char_count.get(char, 0) <= 1 or not 32 < ord(char) < 99])
    return result