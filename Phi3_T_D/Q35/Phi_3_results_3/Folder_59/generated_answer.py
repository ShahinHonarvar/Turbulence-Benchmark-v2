def remove_repeat_chars(s):
    if len(s) < 11:
        return s
    counts = {char: 0 for char in s[0:11]}
    for char in s[0:11]:
        counts[char] += 1
    unique_chars = [char for char in s if counts[char] == 1]
    return ''.join(unique_chars)