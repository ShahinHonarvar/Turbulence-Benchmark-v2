def remove_repeat_chars(input_string):
    target_chars = set(input_string[125:825])
    res = []
    seen = set()
    for char in input_string:
        if char not in seen and char not in target_chars:
            seen.add(char)
            res.append(char)
        elif char in target_chars:
            continue
    return ''.join(res)