def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(33, 78):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (ord(char) < 33 or ord(char) > 78) or count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)