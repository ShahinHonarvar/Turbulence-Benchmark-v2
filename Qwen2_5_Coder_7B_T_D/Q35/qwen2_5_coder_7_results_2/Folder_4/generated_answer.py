def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(50, 74):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (ord(char) < 50 or ord(char) > 74) or count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)