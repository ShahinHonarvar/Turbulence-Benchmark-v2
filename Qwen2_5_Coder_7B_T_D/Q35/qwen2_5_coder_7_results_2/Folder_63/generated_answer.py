def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(81, 86):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (char >= 'A' and char <= 'Z' or (char >= 'a' and char <= 'z')) and count[ord(char)] > 1:
            continue
        result.append(char)
    return ''.join(result)