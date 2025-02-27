def remove_repeat_chars(s):
    unique_chars = set()
    for i in range(2, 6):
        if s[i] in s[2:6] and s.count(s[i]) > 1:
            unique_chars.add(s[i])
    result = ''.join([char for char in s if char not in unique_chars])
    return result