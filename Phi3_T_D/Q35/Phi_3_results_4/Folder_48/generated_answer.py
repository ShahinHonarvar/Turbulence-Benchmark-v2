def remove_repeat_chars(s):
    try:
        limits = (409, 502)
        unique_chars = set(s[limits[0] + 1:limits[1]])
        return ''.join((c for i, c in enumerate(s) if i < limits[0] or i > limits[1] or c not in unique_chars[i - (limits[0] + 1):]))
    except (TypeError, IndexError):
        return s