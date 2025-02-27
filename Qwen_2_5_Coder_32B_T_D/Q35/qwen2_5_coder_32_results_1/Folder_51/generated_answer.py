def remove_repeat_chars(s):
    target = s[7:9]
    counts = {char: target.count(char) for char in target}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))