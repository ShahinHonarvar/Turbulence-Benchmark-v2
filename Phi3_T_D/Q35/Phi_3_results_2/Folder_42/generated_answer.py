def remove_repeat_chars(s):
    start, end = (18, 60)
    char_count = {}
    unique_chars = []
    for i in range(start, end):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count.get(char, 0) > 1 or (start <= s.index(char) < end) == False:
            unique_chars.append(char)
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
    return ''.join(unique_chars)