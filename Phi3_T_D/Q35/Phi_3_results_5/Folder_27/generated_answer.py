def remove_repeat_chars(s):
    start, end = (86, 89)
    count = {}
    result = []
    for i, c in enumerate(s):
        if start <= i < end:
            if c in count:
                result = [char for char in result if char != c]
                count[c] -= 1
            else:
                count[c] = 1
        else:
            result.append(c)
    return ''.join(result)