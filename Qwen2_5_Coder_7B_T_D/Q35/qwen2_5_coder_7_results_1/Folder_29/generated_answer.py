def remove_repeat_chars(s):
    chars_to_remove = [s[i] for i in range(71, 98) if s[i] in s[71:98].count(s[i]) > 1]
    return ''.join([char for char in s if char not in chars_to_remove])