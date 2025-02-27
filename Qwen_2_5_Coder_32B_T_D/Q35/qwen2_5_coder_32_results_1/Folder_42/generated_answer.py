def remove_repeat_chars(s):
    target = s[18:60]
    counts = {}
    for char in target:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    chars_to_remove = {char for char, count in counts.items() if count > 1}
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result