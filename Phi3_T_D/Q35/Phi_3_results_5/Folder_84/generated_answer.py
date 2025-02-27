def remove_repeat_chars(s):
    filtered_indices = {i: s[i] for i in range(32, 44) if s.count(s[i]) > 1}
    return ''.join((c for i, c in enumerate(s) if i not in filtered_indices or c != filtered_indices[i]))