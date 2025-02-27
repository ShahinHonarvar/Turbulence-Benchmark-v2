def remove_repeat_chars(s):
    sub_string = s[462:995]
    seen = set()
    result = []
    for char in sub_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return s[:462] + ''.join(result) + s[995:]