def remove_repeat_chars(s):
    char_count = {}
    for i, char in enumerate(s[25:80]):
        if char in char_count:
            char_count[char] += 1
            if char_count[char] > 1:
                s = s[:i] + s[i + 1:81]
    return s