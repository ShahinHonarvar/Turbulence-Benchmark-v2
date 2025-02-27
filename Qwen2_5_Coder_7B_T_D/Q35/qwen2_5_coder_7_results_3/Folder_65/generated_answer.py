def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(51, 76):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if ord(char) < 51 or ord(char) >= 76 or count[ord(char)] == 1:
            result.append(char)
    return ''.join(result)