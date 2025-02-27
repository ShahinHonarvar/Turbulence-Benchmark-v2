def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(11, 76):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if char.isalpha() and 11 < ord(char) < 76 and (count[ord(char)] > 1) or not char.isalpha():
            continue
        result.append(char)
    return ''.join(result)