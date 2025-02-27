def remove_repeat_chars(s):
    limited_str = s[69:97]
    seen_chars = set()
    output_chars = []
    for char in limited_str:
        if char not in seen_chars:
            seen_chars.add(char)
            output_chars.append(char)
    return s[:69] + ''.join(output_chars) + s[97:]