def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(35, 64):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (ord(char) < 35 or ord(char) > 64) or count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)