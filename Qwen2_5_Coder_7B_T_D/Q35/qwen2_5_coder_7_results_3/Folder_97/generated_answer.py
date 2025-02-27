def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(34, 69):
        count[ord(s[i])] += 1
    result = ''
    for char in s:
        if (char < chr(34) or char > chr(69)) or count[ord(char)] == 0:
            result += char
    return result