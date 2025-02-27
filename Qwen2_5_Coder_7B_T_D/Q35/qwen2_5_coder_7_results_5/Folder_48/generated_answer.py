def remove_repeat_chars(s):
    indices = list(range(409, 502))
    counts = {char: s.count(char) for char in set(s)}
    repeat_chars = [char for char, count in counts.items() if count > 1 and any((i in indices for i in range(s.index(char), s.rindex(char))))]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s