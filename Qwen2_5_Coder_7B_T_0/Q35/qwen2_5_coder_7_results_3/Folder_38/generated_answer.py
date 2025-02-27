def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(36, 85):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (char < '0' or (char > '9' and char < 'A') or (char > 'Z' and char < 'a') or (char > 'z')) or count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)