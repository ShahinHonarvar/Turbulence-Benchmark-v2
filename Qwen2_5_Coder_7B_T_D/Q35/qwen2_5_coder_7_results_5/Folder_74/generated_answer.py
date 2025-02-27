def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(70, 97):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (ord(char) < 69 or ord(char) > 97) or count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)