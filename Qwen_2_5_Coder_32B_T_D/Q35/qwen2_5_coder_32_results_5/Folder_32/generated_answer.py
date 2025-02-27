def remove_repeat_chars(s):
    target = s[87:90]
    counts = {char: target.count(char) for char in set(target)}
    repeats = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeats))