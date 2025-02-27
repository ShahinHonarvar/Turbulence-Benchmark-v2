def remove_repeat_chars(s):
    repeat_chars = set()
    count = [0] * 256
    for i in range(56, 84):
        char = ord(s[i])
        count[char] += 1
        if count[char] > 1:
            repeat_chars.add(char)
    result = []
    for i in range(len(s)):
        char = ord(s[i])
        if char not in repeat_chars:
            result.append(s[i])
    return ''.join(result)