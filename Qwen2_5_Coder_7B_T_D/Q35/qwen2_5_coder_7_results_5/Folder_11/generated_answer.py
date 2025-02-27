def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(49, 76):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if char >= '0' and char <= '9' or (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z'):
            if count[ord(char)] == 1:
                result.append(char)
    return ''.join(result)