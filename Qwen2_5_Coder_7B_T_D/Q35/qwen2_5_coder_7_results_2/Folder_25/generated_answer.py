def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(37, 43):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (char < 'A' or (char > 'Z' and char < 'a') or char > 'z') or count[ord(char)] < 2:
            result.append(char)
    return ''.join(result)