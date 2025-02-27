def remove_repeat_chars(s):
    char_count = {}
    altered_chars = []
    for i, char in enumerate(s):
        if 32 < ord(char) < 99:
            char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count.get(char, 0) > 1 and 32 < ord(char) < 99:
            continue
        altered_chars.append(char)
    return ''.join(altered_chars)