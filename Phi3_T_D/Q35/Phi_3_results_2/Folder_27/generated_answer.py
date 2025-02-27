def remove_repeat_chars(s):
    seen = set()
    output = []
    for i in range(86, 90):
        char = s[i]
        if char in seen:
            continue
        seen.add(char)
        output.append(char)
    return ''.join(output)