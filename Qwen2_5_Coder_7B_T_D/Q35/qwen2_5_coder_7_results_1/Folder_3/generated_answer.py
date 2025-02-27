def remove_repeat_chars(s):
    char_count = [0] * 256
    for i in range(57, 88):
        char_count[ord(s[i])] += 1
    result = []
    for char in s:
        if char_count[ord(char)] == 1 or (ord(char) < 57 or ord(char) > 87):
            result.append(char)
    return ''.join(result)