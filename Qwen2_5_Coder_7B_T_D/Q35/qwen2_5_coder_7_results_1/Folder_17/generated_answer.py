def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(73, 84):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122) and count[ord(char)] > 1:
            continue
        result.append(char)
    return ''.join(result)