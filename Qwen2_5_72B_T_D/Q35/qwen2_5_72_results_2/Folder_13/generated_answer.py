def remove_repeat_chars(s):
    char_count = {}
    for i in range(46, 91):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = [char for char in s if char_count.get(char, 0) <= 1 or (s.index(char) < 46 or s.index(char) > 90)]
    return ''.join(result)