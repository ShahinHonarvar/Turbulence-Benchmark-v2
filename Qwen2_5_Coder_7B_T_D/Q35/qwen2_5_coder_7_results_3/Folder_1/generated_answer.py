def remove_repeat_chars(s):
    repeat_chars = [s[i] for i in range(18, 88) if s.count(s[i]) > 1]
    repeat_chars = set(repeat_chars)
    result = ''.join([char for char in s if char not in repeat_chars])
    return result