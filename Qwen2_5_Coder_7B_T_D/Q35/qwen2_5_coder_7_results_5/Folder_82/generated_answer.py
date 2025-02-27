def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(30, 200):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] < 2 or ((char < 'A' or char > 'Z') and (char < 'a' or char > 'z')):
            result.append(char)
    return ''.join(result)