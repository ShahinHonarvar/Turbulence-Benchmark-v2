def remove_repeat_chars(s):
    count = {}
    for i in range(32, 44):
        char = s[i]
        count[char] = count.get(char, 0) + 1
    return ''.join((char for i, char in enumerate(s) if char not in count or i < 32 or i >= 44))