def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(17, 87):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 1 or not 16 < s.index(char) < 87:
            result.append(char)
    return ''.join(result)