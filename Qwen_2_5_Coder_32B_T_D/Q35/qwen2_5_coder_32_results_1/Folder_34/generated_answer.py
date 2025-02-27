def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    t = s[70:200]
    counts = {}
    for char in t:
        counts[char] = counts.get(char, 0) + 1
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))