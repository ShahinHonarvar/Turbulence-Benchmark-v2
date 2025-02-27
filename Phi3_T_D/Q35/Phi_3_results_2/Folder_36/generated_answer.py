def remove_repeat_chars(s):
    include_indices = (476, 709)
    seen = set()
    result = []
    for i in range(include_indices[0] + 1, include_indices[1]):
        char = s[i]
        if char in seen:
            count = s[include_indices[0] + 1:i].count(char)
            if count > 1:
                s = s.replace(char, '', i - include_indices[0])
        elif i < include_indices[1]:
            seen.add(char)
            result.append(char)
    return ''.join(result)