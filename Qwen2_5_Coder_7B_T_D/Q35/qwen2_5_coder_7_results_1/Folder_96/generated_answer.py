def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(61, 200):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if char >= 'a' and char <= 'z' and (count[ord(char)] == 1) or (char >= 'A' and char <= 'Z' and (count[ord(char)] == 1)) or (ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or ord(char) > 122):
            result.append(char)
    return ''.join(result)