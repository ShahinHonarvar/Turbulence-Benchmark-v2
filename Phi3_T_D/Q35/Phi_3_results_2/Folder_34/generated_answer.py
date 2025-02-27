def remove_repeat_chars(s):
    count = {}
    for i in range(70, 200):
        char = s[i]
        count[char] = count.get(char, 0) + 1
    result = ''.join((char for i, char in enumerate(s) if count[char] == 1 or i < 70 or i >= 200))
    return result