def remove_repeat_chars(s):
    chars = list(s)
    counts = {}
    for i in range(331, 543):
        if chars[i] in counts:
            counts[chars[i]] += 1
        else:
            counts[chars[i]] = 1
    for char, count in counts.items():
        if count > 1:
            for i in range(542, 330, -1):
                if chars[i] == char:
                    chars.pop(i)
    return ''.join(chars)