def remove_repeat_chars(s):
    target_s = s[10:79]
    unique_chars = {char for char in target_s if target_s.count(char) == 1}
    altered_s = ''.join([char for char in s if char not in unique_chars and 10 <= s.index(char) < 79])
    return s[:10] + altered_s + s[79:]