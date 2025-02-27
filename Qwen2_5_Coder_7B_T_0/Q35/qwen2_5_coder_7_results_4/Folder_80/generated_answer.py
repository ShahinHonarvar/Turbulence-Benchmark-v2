def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(57, 84):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (ord(char) < 57 or ord(char) > 84) or count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)