def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(39, 43):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (char < 'a' or char > 'z') and (char < 'A' or char > 'Z'):
            result.append(char)
        elif count[ord(char)] == 1:
            result.append(char)
    return ''.join(result)