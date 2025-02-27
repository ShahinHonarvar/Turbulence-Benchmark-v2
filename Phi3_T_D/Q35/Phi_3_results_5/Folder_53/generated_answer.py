def remove_repeat_chars(s):
    marked_for_removal = set()
    for i in range(201, 203):
        if len(s[i]) > 1:
            for char in s[i]:
                marked_for_removal.add(char)
    result = []
    for char in s:
        if char not in marked_for_removal:
            result.append(char)
    return ''.join(result)