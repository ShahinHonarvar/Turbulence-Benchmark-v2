def remove_repeat_chars(s):
    unique_chars = set()
    to_remove = set()
    for i in range(50, 92):
        char = s[i]
        if char in unique_chars:
            to_remove.add(char)
        else:
            unique_chars.add(char)
    return ''.join([char for char in s if char not in to_remove])