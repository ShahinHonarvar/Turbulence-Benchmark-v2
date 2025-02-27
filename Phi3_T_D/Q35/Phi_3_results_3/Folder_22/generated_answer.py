def remove_repeat_chars(s):
    s_slice = s[50:200]
    unique_chars = ''.join(sorted(set(s_slice), key=s_slice.index))
    exclude_chars = {char for char in set(s_slice) if s_slice.count(char) > 1}
    altered_chars = ''.join([char for char in unique_chars if char not in exclude_chars])
    return s[:50] + altered_chars + s[200:]