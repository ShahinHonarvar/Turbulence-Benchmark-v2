def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(26, 80):
        if s[i] in s[25:80]:
            repeat_chars.add(s[i])
    return ''.join([char for char in s if char not in repeat_chars])