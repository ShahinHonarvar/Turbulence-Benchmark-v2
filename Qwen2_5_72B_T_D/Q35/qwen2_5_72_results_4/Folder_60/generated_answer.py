def remove_repeat_chars(s):
    chars = [0] * 256
    for i in range(38, 52):
        if i < len(s):
            chars[ord(s[i])] += 1
    result = []
    for char in s:
        if chars[ord(char)] < 2:
            result.append(char)
    return ''.join(result)