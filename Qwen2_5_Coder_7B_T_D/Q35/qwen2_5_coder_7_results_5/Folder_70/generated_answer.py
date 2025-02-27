def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(43, 70):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (ord(char) < 43 or ord(char) >= 70) or count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)