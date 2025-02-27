def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(375, 926):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 1 or (ord(char) < 375 or ord(char) >= 926):
            result.append(char)
    return ''.join(result)