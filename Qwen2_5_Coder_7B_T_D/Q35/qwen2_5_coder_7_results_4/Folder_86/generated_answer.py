def remove_repeat_chars(s):
    counted = {}
    for i in range(19, 32):
        if s[i] in counted:
            counted[s[i]] += 1
        else:
            counted[s[i]] = 1
    result = []
    for char in s:
        if (char not in counted or counted[char] == 1) and char != s[0] and (char != s[-1]):
            result.append(char)
    return ''.join(result)