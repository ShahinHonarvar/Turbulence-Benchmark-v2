def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(62, 96):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (ord(char) < 62 or ord(char) > 96) or count[ord(char)] == 0:
            result.append(char)
        else:
            count[ord(char)] = 0
    return ''.join(result)